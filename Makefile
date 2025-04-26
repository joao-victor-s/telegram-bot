# Makefile for managing the furia-bot project with Docker Compose

# Variables
COMPOSE = docker compose
BOT = bot
MONGO = mongo

# Start all services (bot + mongo)
up:
	$(COMPOSE) up --build -d

# Stop and remove all services
down:
	$(COMPOSE) down

# Restart all service
restart:
	$(COMPOSE) restart

# Show real-time logs from the bot service only
logs-bot:
	$(COMPOSE) logs -f $(BOT)

# Show real-time logs from the mongodb service only
logs-mongo:
	$(COMPOSE) logs -f $(MONGO)

# Access the shell of the bot container
shell-bot:
	$(COMPOSE) exec $(BOT) sh

# Access the shell of the mongodb container
shell-mongo:
	$(COMPOSE) exec $(MONGO) sh

# Display help
help:
	@echo "Useful make commands:"
	@echo "  make up          - Build and start all services"
	@echo "  make down        - Stop and remove all services"
	@echo "  make restart     - Restart the bot service"
	@echo "  make logs-bot    - Follow logs from the bot service"
	@echo "  make shell-BOT   - Open an interactive shell in the bot container"
	@echo "  make logs-mongo  - Follow logs from the bot service"
	@echo "  make shell-mongo - Open an interactive shell in the mongo container"
