convert -limit map 0 -limit memory 0 Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project.jpg -crop 256x256 -set filename:tile "%[fx:page.x/256]_%[fx:page.y/256]" +repage +adjoin C:\Web\TileServer\venus\20\tile-%[filename:tile].png

vips dzsave image.jpg output_dir --layout google
