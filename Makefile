help:: ## Список комманд
	@gawk -vG=$$(tput setaf 2) -vR=$$(tput sgr0) ' \
	  match($$0, "^(([^#:]*[^ :]) *:)?([^#]*)##([^#].+|)$$",a) { \
	    if (a[2] != "") { printf "%s\033[36m%-25s\033[0m%s %s\n", G, a[2], R, a[4]; next }\
	    if (a[3] == "") { print a[4]; next }\
	    printf "\n%-36s %s\n","",a[4]\
	  }' $(MAKEFILE_LIST)


.PHONY: push
push: ## Пуш
	@git add .
	@git commit -m "Add Jenkinsfile"
	@git push --set-upstream origin jenkins_task


.PHONY: rebuild
rebuild: ## Пересобрать контейнеры
	@docker compose down
	@docker compose up -d
