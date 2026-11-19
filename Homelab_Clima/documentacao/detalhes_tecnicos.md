# Detalhes Técnicos da Infraestrutura

Para garantir a resiliência e a segurança do pipeline, a infraestrutura foi configurada da seguinte forma:

## 1. Servidor (Tablet Android com Termux)
O tablet (2GB RAM) atua como servidor de banco de dados e arquivos.
- **Gerenciamento de Serviços:** Uso do `termux-services` (runit) para garantir que os processos (MySQL, GoTTY, FileBrowser, SSH) reiniciem automaticamente em caso de falha.
- **Otimização de RAM:** Os serviços críticos são iniciados via `sv` (runit) e o script de boot foi enxugado para evitar conflitos de porta e consumo excessivo de memória.
- **Segurança:** O banco de dados não é exposto à internet aberta. O acesso é feito exclusivamente via VPN (Tailscale).

## 2. Processamento e BI (PC com Docker)
- **Apache Airflow:** Roda em containers Docker e orquestra o ETL diário.
- **Metabase:** Também em Docker, conecta-se ao banco via IP da VPN Tailscale para gerar os dashboards.

## 3. Acesso Remoto e Notificação (Cloudflare + Watchdog)
- **Cloudflare Tunnel:** Expõe o GoTTY e o FileBrowser de forma segura.
- **Watchdog de Túneis (Python):** Como o Cloudflare Quick Tunnel gera uma URL dinâmica a cada reinício, foi criado um script (`watchdog_tunnels.py`) que monitora o log do túnel. Se a URL mudar, ele envia um e-mail automaticamente com o novo link, garantindo que o acesso remoto nunca seja perdido.

## 4. Configuração do Banco de Dados
O acesso remoto ao MariaDB foi liberado via rede local (Tailscale), com criação de usuário específico para o Airflow e Metabase (evitando o uso do root para maior segurança).