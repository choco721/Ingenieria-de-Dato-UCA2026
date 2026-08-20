# =============================================================================
#  Atajos del stack. En vez de comandos largos de docker compose, usás:
#     make up      -> levanta todo
#     make ps      -> ver qué está corriendo
#     make down    -> apaga (conserva los datos)
#     make clean   -> apaga Y BORRA los datos (usar solo si algo está muy roto)
#     make logs    -> ver los logs en vivo
#     make restart -> reiniciar todo
# =============================================================================

.PHONY: up ps down clean logs restart

up:
	docker compose up -d --build

ps:
	docker compose ps

down:
	docker compose down

# OJO: clean borra los volúmenes = borra TODOS los datos guardados.
clean:
	docker compose down -v

logs:
	docker compose logs -f

restart:
	docker compose down && docker compose up -d
