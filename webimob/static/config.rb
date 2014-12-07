# =============================================================================
# usage:
# entrar no diretorio onde o arquivo config.rb estiver e executar como abaixo:
# padrao: /home/(usuario)/project/static
# =============================================================================
# development mode:
# => compass compile
# production mode:
# => compass compile -e production
# =============================================================================

css_dir = "css"
sass_dir = "scss"
images_dir = "images"
javascripts_dir = "js"

if environment == :production
	http_path = "http://static.webimob.ambiente-dev.com.br/"
	http_images_path = "http://static.webimob.ambiente-dev.com.br/images"
	http_generated_images_path = "http://static.webimob.ambiente-dev.com.br/images"
	output_style = :compressed
	line_comments = false
else
	http_path = "/"
	http_images_path = "/static/images"
	http_generated_images_path = "/static/images"
	output_style = :expanded
end