Pour le projet my_rpg, pouvoir créer des map est indispensable. Tiled est une application qui vous permet facilement de créer vos propres map et de les exporter sous différents formats.

L'objectif de ce #CODE est de vous faire découvrir Tiled et de vous donner des pistes sur comment vous allez pouvoir aussi l'utiliser pour gérer vos collisions.

# Installer Tiled

Allez sur ce lien:
https://thorbjorn.itch.io/tiled
et installez la version Ubuntu.

> [!NOTE] INFO
> C'est un AppImage, si vous ne savez pas comment l'utiliser, allez voir cette page
> https://www.itprotoday.com/development-techniques-and-management/why-and-how-use-appimage-ubuntu

Normalement Tiled devrait se lancer.

# Chercher une Tileset

Une tileset est un ensemble d'images (tile) qui représentent différents éléments d'un environnement (sols, murs...).
Vous pouvez retrouver des tileset gratuits sur différents sites comme https://itch.io/game-assets
ou si vous ne voulez pas vous embêter en voilà une:
https://cupnooble.itch.io/sprout-lands-asset-pack
Les tilesets ont différentes tailles (16x16, 32x32, 64x64....). Il est important si vous utilisez plusieurs tileset de garder la même taille.

# Créer une carte

Commencez par créer une carte et donnez lui la taille que vous voulez. Pour ce qui est de la taille des tuiles, mettez la même que vos tilesets.

Une fois validé, vous vous retrouverez avec une carte vide.

# Importer une Tileset

Pour importer une Tileset, vous pouvez cliquer sur  *Nouveau Jeu de Tuiles*, donnez la tileset que vous souhaitez utiliser et vérifiez bien que la longueur et largeur des tuiles soit la bonne.

# Dessiner votre Map

Pour dessiner vous pouvez sélectionnner une ou plusieurs tiles de votre Tilemap et dessiner avec le tampon. Vous pouvez aussi utiliser l'outil *Remplissage* pour remplir directement certaines zones.

Vous pouvez aussi créer de nouveaux calques pour superposer différents éléments.

# Exporter votre Map

Une fois que vous êtes satisfait du résultat, vous devez ensuite exporter votre Map. Pour cela, il suffit d'aller dans *fichier->Exporter en tant qu'Image*. Vous aurez ensuite votre map en format image ce qui vous permettra dans votre RPG de l'afficher facilement.

# Pour aller plus loin - Les Collisions

Lorsque vous allez commencer à implémenter vos maps dans votre rpg, vous allez aussi vouloir gérer les collisions. Sauf qu'elles sont propres aux maps et écrire manuellement les collisions ça peut être rapidement très long. Tiled permet aussi d'exporter les maps au format json ce qui est très pratique, car on peut récupérer les différents calques et les traiter.

La première étape est de faire un nouveau calque appelé "Collision" où chaque tuile de posé sera considéré comme collision. À vous de les dessiner.
(Peut importe la tile que vous utilisez pour dessiner les collision, on va cacher le calque lors de l'export de la map, elle servira juste pour connaître la position des collisions)

Ensuite, exportez la map en json.

Maintenant, vous allez retrouver dans le repo un fichier tiled-to-c.py qui va vous permettre à partir du fichier json de vous ressortir un fichier .coll avec à l'intérieur la position en (x, y) des collisions.

Cependant, à vous de le compléter :)
