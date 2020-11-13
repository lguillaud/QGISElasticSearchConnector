<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="fr_FR">
<context>
    <name>ConnectionDialog</name>
    <message>
        <location filename="../ConnectionDialog.py" line="77"/>
        <source>Save Connection</source>
        <translation>Sauvegarder la connexion</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="77"/>
        <source>Should the existing connection {0} be overwritten?</source>
        <translation>La connexion existante {0} doit-elle être écrasée ?</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="85"/>
        <source>Saving Passwords</source>
        <translation>Sauvegarde de mot de passe</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="85"/>
        <source>WARNING: You have entered a password. It will be stored in unsecured plain text in your project files and your home directory (Unix-like OS) or user profile (Windows). If you want to avoid this, press Cancel and either:

a) Don&apos;t provide a password in the connection settings â it will be requested interactively when needed;
b) Use the Configuration tab to add your credentials in an HTTP Basic Authentication method and store them in an encrypted database.</source>
        <translation>ATTENTION: Vous avez saisi un mot de passe. Il sera stocké en calir dans vos fichiers de projet et dans votre répertoire personnel ou votre profil utilisateur. Si vous ne le souhaitez pas, appuyez sur Annuler et, au choix,:

a) Ne saisissez pas un mot de passe dans les paramètres de connexion: il sera demandé interactivement quand nécessaire;
b) Utilisez l&apos;onglet de Configuration pour ajouter votre mot de passe dans une méthode Authentification Basique HTTP pour le stocker dans une base de données cryptée.</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="44"/>
        <source>Modify Connection</source>
        <translation>Modification de Connexion</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="64"/>
        <source>none</source>
        <translation>aucun(e)</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="174"/>
        <source>Test connection</source>
        <translation>Tester la connexion</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="170"/>
        <source>Connection to {0} was successful</source>
        <translation>Connection à {0} réussie</translation>
    </message>
    <message>
        <location filename="../ConnectionDialog.py" line="174"/>
        <source>Cannot connect to {0}.
Reason: {1}</source>
        <translation>Impossible de se connecter à {0}.
Raison: {1}</translation>
    </message>
</context>
<context>
    <name>ConnectionDialogBase</name>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="14"/>
        <source>Create a New Connection</source>
        <translation>Créer une Nouvelle Connection</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="33"/>
        <source>Connection Details</source>
        <translation>Détails de connexion</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="104"/>
        <source>Name</source>
        <translation>Nom</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="123"/>
        <source>Name of the new connection</source>
        <translation>Nom de la nouvelle connexion</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="133"/>
        <source>URL</source>
        <translation>URL</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="143"/>
        <source>HTTP address of the Elasticsearch Server</source>
        <translation>Adresse HTTP du serveur Elasticsearch</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="213"/>
        <source>&amp;Test Connection</source>
        <translation>&amp;Tester la connexion</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="109"/>
        <source>Options</source>
        <translation type="obsolete">Options</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="39"/>
        <source>Authentication</source>
        <translation>Authentification</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="153"/>
        <source>Feature retrieval related options</source>
        <translation>Options liées à la récupération des entités</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="159"/>
        <source>Batch size</source>
        <translation>Taille de la page</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="166"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Enter a number to limit the maximum number of documents retrieved in a single scrolling request. If let to empty, it will default to 100.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Entrez un nombre pour limiter le nombre maximum de documents à télécharger lors d&apos;une requête unitaire. La valeur par défaut est 100.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="186"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Enter a number to limit the maximum number of documents retrieved during feature iteration&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Entrez un nombre pour limiter le nombre maximum de documents à télécharger lors de l&apos;itération sur les entités.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="311"/>
        <source>unlimited</source>
        <translation>illimité</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="318"/>
        <source>Timeout (second)</source>
        <translation>Délai d&apos;abandon (seconde)</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="203"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Maximum delay in second allowed for feature iteration&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Délai maximum en seconnde autorisé pour l&apos;itération sur les entités.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="220"/>
        <source>Feature definition related options</source>
        <translation>Options liées à l&apos;établissement de la définition des entités</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="236"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Enter a number to limit the maximum number of documents retrieved to establish the feature definition (fields, geometry type). If let to empty, it will default to 100 documents.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Entrez un nombre pour limiter le nombre maximum de documents à télécharger pour établir la définition des entités (champs, type de géométrie). La valeur par défaut est 100.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="249"/>
        <source>FID property name</source>
        <translation>Nom de la propriété pour l&apos;ID d&apos;entité</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="256"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Enter the name of the property that must be used to fill the OGR feature identifier. It will default to ogc_fid&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Entrez le nom de la propriété à utiliser pour remplir l&apos;identifiant d&apos;entité OGR. La valeur par défaut est ogc_fid.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="266"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Whether to include a field with the full document as JSON.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Si un champ doit être ajouté avec le contenu du document en JSON.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="269"/>
        <source>Include JSON document in a field</source>
        <translation>Inclure le document JSON dans un champ</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="276"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Whether to recursively explore nested objects and produce flatten OGR attributes.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Si la structure hiérarchique des documents doit être aplatie pour produire les attributs OGR.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="279"/>
        <source>Flatten nested attributes</source>
        <translation>Aplatir les attributs imbriqués</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="292"/>
        <source>Single requests (extent, feature count retrieval) related options</source>
        <translation>Options liées aux requêtes unitaires (obtention d&apos;emprise et nombre d&apos;entités)</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="308"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Enter a number to limit the maximum number of documents retrieved during a single request&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Entrez un nombre pour limiter le nombre maximum de documents à télécharger pour une requête unitaire.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="325"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Maximum delay in second allowed for a single request&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Délai maximum en seconnde autorisé pour les requêtes unitaires.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionDialog.ui" line="298"/>
        <source>Max. document count</source>
        <translation>Nombre max. de documents</translation>
    </message>
</context>
<context>
    <name>ConnectionsDialog</name>
    <message>
        <location filename="../ConnectionsDialog.py" line="89"/>
        <source>&amp;Add</source>
        <translation>&amp;Ajouter</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="90"/>
        <source>Add selected layers to map</source>
        <translation>Ajouter les couches sélectionnées à la carte</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="95"/>
        <source>Close this dialog without adding any layer</source>
        <translation>Fermer cette boite de dialogue sans ajouter de couche</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="106"/>
        <source>Name</source>
        <translation>Nom</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="103"/>
        <source>Sql</source>
        <translation type="obsolete">Sql</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="166"/>
        <source>Are you sure you want to remove the {0} connection and all associated settings?</source>
        <translation>Etes-vous certain de vouloir supprimer la connection {0} et les paramètres associés ?</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="168"/>
        <source>Confirm Delete</source>
        <translation>Confirmation de Suppression</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="81"/>
        <source>&amp;Build query</source>
        <translation>Constr&amp;uire une requête</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="82"/>
        <source>Build query</source>
        <translation>Construire une requête</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="108"/>
        <source>Geometry type</source>
        <translation>Type de géométrie</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="208"/>
        <source>Connection Error</source>
        <translation>Erreur de connexion</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="208"/>
        <source>Cannot connect to {0}.
Reason: {1}</source>
        <translation>Impossible de se connecter à {0}.
Raison: {1}</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="110"/>
        <source>Sql or Elasticsearch JSON query</source>
        <translation>Sql ou requête JSON Elasticsearch</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="325"/>
        <source>Load Connections</source>
        <translation>Chargement de connexions</translation>
    </message>
    <message>
        <location filename="../ConnectionsDialog.py" line="325"/>
        <source>XML files (*.xml *.XML)</source>
        <translation>Fichiers XML (*.xml *.XML)</translation>
    </message>
</context>
<context>
    <name>Connector</name>
    <message>
        <location filename="../Connector.py" line="62"/>
        <source>&amp;Elasticsearch Connector</source>
        <translation type="obsolete">Connecteur &amp;Elasticsearch</translation>
    </message>
    <message>
        <location filename="../Connector.py" line="53"/>
        <source>Elasticsearch Connector</source>
        <translation type="obsolete">Connecteur Elasticsearch</translation>
    </message>
    <message>
        <location filename="../Connector.py" line="71"/>
        <source>Add &amp;Elasticsearch Layerâ¦</source>
        <translation type="obsolete">Ajouter une couche Elasticsearch…</translation>
    </message>
    <message>
        <location filename="../Connector.py" line="84"/>
        <source>Elasticsearch</source>
        <translation type="obsolete">Elasticsearch</translation>
    </message>
</context>
<context>
    <name>ElasticSearchConnectionDialogBase</name>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="14"/>
        <source>Add Elasticsearch Layer</source>
        <translation>Ajouter une couche Elasticsearch</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="39"/>
        <source>Server Connections</source>
        <translation>Connexions aux serveurs</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="53"/>
        <source>Connect to selected service</source>
        <translation>Se connecter au service sélectionné</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="56"/>
        <source>C&amp;onnect</source>
        <translation>C&amp;onnexion</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="63"/>
        <source>Create a new service connection</source>
        <translation>Créer une nouvelle connection</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="66"/>
        <source>&amp;New</source>
        <translation>&amp;Nouveau</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="76"/>
        <source>Edit selected service connection</source>
        <translation>Modifier la connection sélectionnée</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="79"/>
        <source>Edit</source>
        <translation>Modifier</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="89"/>
        <source>Remove connection to selected service</source>
        <translation>Supprimer la connexion au service sélectionné</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="92"/>
        <source>Remove</source>
        <translation>Supprimer</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="115"/>
        <source>Load connections from file</source>
        <translation>Charger des connexions depuis un fichier</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="118"/>
        <source>Load</source>
        <translation>Charger</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="125"/>
        <source>Save connections to file</source>
        <translation>Enregister des connexions dans un fichier</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="128"/>
        <source>Save</source>
        <translation>Enregistrer</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="145"/>
        <source>Fil&amp;ter</source>
        <translation>Filtre</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="161"/>
        <source>Display indices containing this word in their name</source>
        <translation>Afficher les indexes contenant ce mot dans leur nom</translation>
    </message>
</context>
<context>
    <name>ElasticSearchConnector</name>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="49"/>
        <source>Layer title</source>
        <translation type="obsolete">Titre de la couche</translation>
    </message>
    <message>
        <location filename="../Ui_ConnectionsDialog.ui" line="123"/>
        <source>About</source>
        <translation type="obsolete">A propos de</translation>
    </message>
    <message>
        <location filename="../DataItems.py" line="132"/>
        <source>Elasticsearch</source>
        <translation>Elasticsearch</translation>
    </message>
    <message>
        <location filename="../DataItems.py" line="148"/>
        <source>Manage connectionsâ¦</source>
        <translation>Gérer les connexions…</translation>
    </message>
    <message>
        <location filename="../DataItems.py" line="155"/>
        <source>Refresh</source>
        <translation>Rafraîchir</translation>
    </message>
    <message>
        <location filename="../Connector.py" line="53"/>
        <source>Elasticsearch Connector</source>
        <translation>Connecteur Elasticsearch</translation>
    </message>
    <message>
        <location filename="../Connector.py" line="60"/>
        <source>&amp;Elasticsearch Connector</source>
        <translation>Connecteur &amp;Elasticsearch</translation>
    </message>
    <message>
        <location filename="../Connector.py" line="69"/>
        <source>Add &amp;Elasticsearch Layer...</source>
        <translation>Ajouter une couche Elasticsearch…</translation>
    </message>
</context>
<context>
    <name>ImportExportConnectionsDialog</name>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="48"/>
        <source>Select all</source>
        <translation>Tout sélectionner</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="52"/>
        <source>Clear selection</source>
        <translation>Effacer la sélection</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="57"/>
        <source>Import Connections</source>
        <translation>Import de connexions</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="58"/>
        <source>Select connections to import</source>
        <translation>Sélectionner les connexions à importer</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="60"/>
        <source>Import</source>
        <translation>Import</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="63"/>
        <source>Export Connections</source>
        <translation>Export de connexions</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="65"/>
        <source>Export</source>
        <translation>Export</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="228"/>
        <source>Loading Connections</source>
        <translation>Chargement de connexions</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="81"/>
        <source>Cannot read file {0}:
{1}.</source>
        <translation>Impossible de lire le fichier {0}:
{1}</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="89"/>
        <source>Parse error at line {0}, column {1}:
{2}</source>
        <translation>Erreur d&apos;analyse à la ligne {0}, colonne {1}:
{2}</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="99"/>
        <source>The file is not a Elasticsearch connections exchange file.</source>
        <translation>Le fichier n&apos;est pas un fichier d&apos;échange de connexions Elasticsearch</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="127"/>
        <source>Export/Import Error</source>
        <translation>Erreur d&apos;import/export</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="127"/>
        <source>You should select at least one connection from list.</source>
        <translation>Vous devez sélectionner au moins une connexion dans la liste.</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="135"/>
        <source>Save Connections</source>
        <translation>Sauvergarde de connexions</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="135"/>
        <source>XML files (*.xml *.XML)</source>
        <translation>Fichiers XML (*.xml *.XML)</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="148"/>
        <source>Saving Connections</source>
        <translation>Sauvegarde de connexions</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="148"/>
        <source>Cannot write file {0}:
{1}.</source>
        <translation>Impossible d&apos;écrire le fichier {0}:
{1}.</translation>
    </message>
    <message>
        <location filename="../ImportExportConnectionsDialog.py" line="228"/>
        <source>Connection with name &apos;{0}&apos; already exists. Overwrite?</source>
        <translation>Une connexion de nom &apos;{0}&apos; existe déjà. Souhaitez-vous l&apos;écraser ?</translation>
    </message>
</context>
<context>
    <name>ImportExportConnectionsDialogBase</name>
    <message>
        <location filename="../Ui_ImportExportConnectionsDialog.ui" line="14"/>
        <source>Import/export connections</source>
        <translation>Import/export de connexions</translation>
    </message>
    <message>
        <location filename="../Ui_ImportExportConnectionsDialog.ui" line="20"/>
        <source>Select connections to export</source>
        <translation>Sélectionner les connexions à exporter</translation>
    </message>
</context>
<context>
    <name>QgsQueryBuilder</name>
    <message>
        <location filename="../QueryBuilder.py" line="89"/>
        <source>Query Result</source>
        <translation>Résultat de la requête</translation>
    </message>
    <message>
        <location filename="../QueryBuilder.py" line="89"/>
        <source>An error occurred when executing the query.</source>
        <translation>Une erreur est survenue durant l&apos;exécution de la requête</translation>
    </message>
    <message>
        <location filename="../QueryBuilder.py" line="81"/>
        <source>
The data provider said:
%1</source>
        <translation>La fournisseur de données indique:
%1</translation>
    </message>
    <message>
        <location filename="../QueryBuilder.py" line="71"/>
        <source>An error occurred when executing the query, please check the expression syntax.</source>
        <translation>Une ereur est survenue durant l&apos;exécution de la requête. Veuillez vérifier la syntax de l&apos;expression.</translation>
    </message>
    <message numerus="yes">
        <location filename="../QueryBuilder.py" line="76"/>
        <source>The where clause returned %n row(s).</source>
        <comment>returned test rows</comment>
        <translation>
            <numerusform>La requête a retournée %n enregistrement.</numerusform>
            <numerusform>La requête a retournée %n enregistrement.</numerusform>
        </translation>
    </message>
</context>
<context>
    <name>QueryBuilder</name>
    <message>
        <location filename="../QueryBuilder.py" line="38"/>
        <source>Enter SQL request or ElasticSearch query (JSON)</source>
        <translation>Saisissez une requête SQL ou Elasticsearch (JSON)</translation>
    </message>
</context>
</TS>
