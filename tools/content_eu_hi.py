"""Spanish, Portuguese, French, German and Hindi content for the privacy policy."""

from content_en_zh import SUPPORT_URL

_GH = ("https://docs.github.com/en/site-policy/privacy-policies/"
       "github-general-privacy-statement")

ES = {
    "code": "es",
    "html_lang": "es",
    "label": "Español",
    "dir": "ltr",
    "doc_title": "Numeria — Política de privacidad",
    "h1": "Política de privacidad",
    "product": "<strong>Numeria: Calculadoras financieras</strong> &middot; versión 1.0.0 &middot; iOS (iPhone)",
    "effective": "Fecha de entrada en vigor: 13 de septiembre de 2026",
    "tldr_head": "En una frase",
    "tldr": "Numeria no recopila nada. Sin cuenta, sin anuncios, sin analíticas y sin servidor: "
            "todos los cálculos se realizan íntegramente en tu dispositivo y las cifras que "
            "introduces nunca se guardan ni se transmiten.",
    "blocks": [
        ("h2", "1. Lo que no recopilamos"),
        ("p", "Numeria no tiene ningún componente de servidor y la aplicación no realiza "
              "solicitudes de red propias. Por tanto, no podemos recopilar —y nunca hemos "
              "recopilado— lo siguiente:"),
        ("ul", [
            "identificadores personales como tu nombre, correo electrónico, número de teléfono o fecha de nacimiento",
            "datos de cuentas financieras, como números de cuenta bancaria, de tarjeta o de corretaje",
            "ubicación precisa o aproximada",
            "contactos, fotos, datos de salud ni ningún otro contenido de tu dispositivo",
            "analíticas de uso, perfiles de comportamiento ni el identificador publicitario (IDFA)",
        ]),
        ("p", "Como no se recopila nada en primer lugar, no hay nada que pueda compartirse con "
              "terceros, venderse o verse expuesto en una brecha. La etiqueta de privacidad de "
              "Numeria en el App Store es <strong>«No se recopilan datos» (Data Not Collected)</strong>."),

        ("h2", "2. Lo que se guarda en tu dispositivo"),
        ("p", "Numeria escribe una pequeña cantidad de datos en el almacén de preferencias local "
              "de tu dispositivo para recordar tus elecciones entre sesiones. Estos datos nunca "
              "salen de tu dispositivo y nosotros no podemos leerlos:"),
        ("table", {
            "head": ["Dato guardado", "Para qué sirve"],
            "rows": [
                ["Identificadores de las últimas 10 calculadoras que abriste",
                 "Rellenan la lista «Recientes» de la pantalla de inicio"],
                ["Identificadores de las calculadoras marcadas como favoritas",
                 "Rellenan tu lista «Favoritas»"],
                ["Preferencia de símbolo de moneda",
                 "Formatea los importes como esperas"],
                ["Preferencia de tema (claro, oscuro o del sistema)",
                 "Aplica la apariencia que elegiste"],
                ["Preferencia de idioma",
                 "Muestra la interfaz en tu idioma"],
                ["Marca de desbloqueo",
                 "Recuerda que compraste «Desbloquear todo» para no cobrarte dos veces"],
            ],
        }),
        ("note", "<strong>Las cifras que introduces no se guardan.</strong> Ninguna entrada, valor "
                 "intermedio o resultado de las calculadoras se escribe en disco ni se envía a "
                 "ningún sitio. Al cerrar una calculadora se descarta lo que escribiste en ella."),

        ("h2", "3. Compras"),
        ("p", "Numeria ofrece una única compra integrada no consumible, «Desbloquear todas las "
              "calculadoras». El pago lo procesa íntegramente Apple a través del App Store y "
              "StoreKit. Nosotros nunca vemos, recibimos ni guardamos tu método de pago, número "
              "de tarjeta, Apple ID o historial de compras."),
        ("p", "El único dato relacionado con la compra que conserva la aplicación es la marca de "
              "desbloqueo local descrita arriba. Cuando usas <em>Restaurar compras</em>, la "
              "aplicación consulta el App Store directamente desde tu dispositivo; la respuesta "
              "sirve únicamente para establecer esa marca y no se nos reenvía. Los reembolsos los "
              "gestiona Apple según sus propias políticas."),

        ("h2", "4. Terceros"),
        ("p", "Numeria no integra SDK de terceros: ni redes publicitarias, ni proveedores de "
              "analíticas, ni SDK de redes sociales, ni herramientas de informe de fallos. Los "
              "únicos servicios de plataforma con los que se comunica son:"),
        ("ul", [
            "el App Store de Apple, exclusivamente para validar la compra integrada, y",
            "el navegador externo de tu dispositivo, cuando pulsas los enlaces <em>Soporte</em> o "
            "<em>Política de privacidad</em> en Ajustes y el sistema abre esa URL fuera de la aplicación.",
        ]),

        ("h2", "5. Sobre esta página web"),
        ("p", "La aplicación no recopila nada, pero este documento está alojado en GitHub Pages "
              "para que el App Store disponga de una URL a la que enlazar. Al cargarla, GitHub "
              "puede registrar información estándar de registro del servidor —como tu dirección "
              "IP, el tipo de navegador y la hora de la solicitud— conforme a la "
              "<a href=\"" + _GH + "\" rel=\"noopener\">propia declaración de privacidad de GitHub</a>. "
              "Nosotros no recibimos esos registros ni tenemos acceso a ellos."),
        ("p", "Esta página no carga fuentes, scripts, hojas de estilo, imágenes ni rastreadores "
              "externos. Lo único que escribe en tu navegador es el idioma que has elegido, para "
              "que la página se abra en ese mismo idioma la próxima vez."),

        ("h2", "6. Menores"),
        ("p", "Numeria es una herramienta de cálculo de uso general con clasificación 4+. No está "
              "dirigida a menores y no recopila datos de nadie, menores incluidos."),

        ("h2", "7. Conservación y eliminación de datos"),
        ("p", "No existe ninguna copia de tus datos en un servidor, así que no tenemos nada que "
              "conservar, exportar ni eliminar. Para borrar todo rastro de los datos que Numeria "
              "haya escrito, simplemente elimina la aplicación: desinstalarla borra las "
              "preferencias locales enumeradas en la sección 2."),

        ("h2", "8. Tus derechos"),
        ("p", "Como Numeria no conserva ningún dato personal sobre ti, no hay datos personales que "
              "podamos revelar, corregir, exportar o suprimir a petición tuya. Los derechos que "
              "reconocen el RGPD, la CCPA y normas similares recaen sobre datos personales, y esta "
              "aplicación no genera ninguno. Si crees que algo de esta página es inexacto, "
              "dínoslo y lo corregiremos."),

        ("h2", "9. Cambios en esta política"),
        ("p", "Si una versión futura de Numeria modifica algo de lo aquí descrito —por ejemplo, si "
              "añadiéramos sincronización opcional en la nube o cualquier función con conexión— "
              "actualizaremos esta página, revisaremos la fecha de entrada en vigor y revelaremos "
              "el cambio en las notas de la versión del App Store antes de publicar esa versión."),

        ("h2", "10. Contacto"),
        ("p", "Para preguntas sobre esta política o sobre la aplicación: "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a>"),
        ("p", "Desarrollador: <strong>wanggit</strong> (desarrollador individual), editor de "
              "<em>Numeria: Calculadoras financieras</em> en el App Store."),
    ],
    "disclaimer_head": "No es asesoramiento financiero",
    "disclaimer": "Numeria produce estimaciones aritméticas con fines de planificación. Sus "
                  "resultados no constituyen asesoramiento financiero, fiscal, jurídico ni de "
                  "inversión, y no tienen en cuenta todas tus circunstancias. Consulta a un "
                  "profesional cualificado antes de actuar basándote en cualquier cifra que la "
                  "aplicación te muestre.",
}

PT = {
    "code": "pt",
    "html_lang": "pt",
    "label": "Português",
    "dir": "ltr",
    "doc_title": "Numeria — Política de Privacidade",
    "h1": "Política de Privacidade",
    "product": "<strong>Numeria: Calculadoras financeiras</strong> &middot; versão 1.0.0 &middot; iOS (iPhone)",
    "effective": "Data de vigência: 13 de setembro de 2026",
    "tldr_head": "Em uma frase",
    "tldr": "A Numeria não coleta nada. Sem conta, sem anúncios, sem análise de dados e sem "
            "servidor: todo cálculo acontece inteiramente no seu aparelho, e os números que você "
            "digita nunca são armazenados nem transmitidos.",
    "blocks": [
        ("h2", "1. O que não coletamos"),
        ("p", "A Numeria não possui nenhum componente de servidor e o aplicativo não faz "
              "solicitações de rede próprias. Portanto, não podemos coletar — e nunca coletamos — "
              "o seguinte:"),
        ("ul", [
            "identificadores pessoais, como nome, e-mail, número de telefone ou data de nascimento",
            "dados de contas financeiras, como números de conta bancária, de cartão ou de corretora",
            "localização precisa ou aproximada",
            "contatos, fotos, dados de saúde ou qualquer outro conteúdo do seu aparelho",
            "análise de uso, perfis comportamentais ou o identificador de publicidade (IDFA)",
        ]),
        ("p", "Como nada é coletado em primeiro lugar, não há nada que possa ser compartilhado com "
              "terceiros, vendido ou vazado. O rótulo de privacidade da Numeria na App Store é "
              "<strong>«Dados não coletados» (Data Not Collected)</strong>."),

        ("h2", "2. O que fica armazenado no seu aparelho"),
        ("p", "A Numeria grava uma pequena quantidade de dados no armazenamento local de "
              "preferências do seu aparelho para lembrar suas escolhas entre as aberturas. Esses "
              "dados nunca saem do aparelho e não podem ser lidos por nós:"),
        ("table", {
            "head": ["Dado armazenado", "Para que serve"],
            "rows": [
                ["Identificadores das últimas 10 calculadoras que você abriu",
                 "Preenchem a lista «Recentes» na tela inicial"],
                ["Identificadores das calculadoras marcadas como favoritas",
                 "Preenchem sua lista «Favoritas»"],
                ["Preferência de símbolo de moeda",
                 "Formata os valores monetários como você espera"],
                ["Preferência de tema (claro, escuro ou do sistema)",
                 "Aplica a aparência que você escolheu"],
                ["Preferência de idioma",
                 "Exibe a interface no seu idioma"],
                ["Marcador de desbloqueio",
                 "Lembra que você comprou «Desbloquear tudo», para nunca cobrar duas vezes"],
            ],
        }),
        ("note", "<strong>Os números que você digita não são salvos.</strong> Nenhuma entrada, "
                 "valor intermediário ou resultado de calculadora é gravado em disco nem enviado "
                 "a qualquer lugar. Ao fechar uma calculadora, o que você digitou é descartado."),

        ("h2", "3. Compras"),
        ("p", "A Numeria oferece uma única compra integrada não consumível, «Desbloquear todas as "
              "calculadoras». O pagamento é processado integralmente pela Apple, por meio da App "
              "Store e do StoreKit. Nós nunca vemos, recebemos ou armazenamos sua forma de "
              "pagamento, número de cartão, Apple ID ou histórico de compras."),
        ("p", "O único dado relacionado à compra que o aplicativo mantém é o marcador local de "
              "desbloqueio descrito acima. Quando você usa <em>Restaurar compras</em>, o "
              "aplicativo consulta a App Store diretamente do seu aparelho; a resposta serve "
              "apenas para definir esse marcador e não nos é encaminhada. Reembolsos são "
              "tratados pela Apple conforme suas próprias políticas."),

        ("h2", "4. Terceiros"),
        ("p", "A Numeria não incorpora SDKs de terceiros — nem redes de publicidade, nem "
              "provedores de análise, nem SDKs de redes sociais, nem relatórios de falhas. Os "
              "únicos serviços de plataforma com os quais se comunica são:"),
        ("ul", [
            "a App Store da Apple, exclusivamente para validar a compra integrada, e",
            "o navegador externo do seu aparelho, quando você toca nos links <em>Suporte</em> ou "
            "<em>Política de Privacidade</em> em Ajustes e o sistema abre essa URL fora do aplicativo.",
        ]),

        ("h2", "5. Sobre esta página"),
        ("p", "O aplicativo não coleta nada, mas este documento está hospedado no GitHub Pages "
              "para que a App Store tenha uma URL para vincular. Ao carregá-la, o GitHub pode "
              "registrar informações padrão de log do servidor — como seu endereço IP, tipo de "
              "navegador e hora da solicitação — nos termos da "
              "<a href=\"" + _GH + "\" rel=\"noopener\">própria declaração de privacidade do GitHub</a>. "
              "Nós não recebemos esses logs nem temos acesso a eles."),
        ("p", "Esta página não carrega fontes, scripts, folhas de estilo, imagens nem "
              "rastreadores externos. A única coisa que ela grava no seu navegador é o idioma "
              "escolhido, para que a página reabra no mesmo idioma da próxima vez."),

        ("h2", "6. Crianças"),
        ("p", "A Numeria é uma ferramenta de cálculo de uso geral com classificação 4+. Não é "
              "direcionada a crianças e não coleta dados de ninguém — incluindo crianças."),

        ("h2", "7. Retenção e exclusão de dados"),
        ("p", "Não existe nenhuma cópia dos seus dados em servidor, então não há nada para "
              "retermos, exportarmos ou excluirmos. Para remover todo vestígio dos dados que a "
              "Numeria gravou, basta apagar o aplicativo: desinstalar apaga as preferências "
              "locais listadas na seção 2."),

        ("h2", "8. Seus direitos"),
        ("p", "Como a Numeria não guarda nenhum dado pessoal sobre você, não há dados pessoais a "
              "divulgar, corrigir, exportar ou apagar mediante solicitação. Os direitos previstos "
              "no GDPR, na CCPA e em regimes semelhantes incidem sobre dados pessoais, e este "
              "aplicativo não cria nenhum. Se você achar que algo nesta página está incorreto, "
              "avise-nos e corrigiremos."),

        ("h2", "9. Alterações desta política"),
        ("p", "Se uma versão futura da Numeria alterar qualquer coisa aqui descrita — por exemplo, "
              "se acrescentarmos sincronização opcional em nuvem ou qualquer recurso de rede — "
              "atualizaremos esta página, revisaremos a data de vigência acima e divulgaremos a "
              "alteração nas notas de versão da App Store antes de lançar aquela versão."),

        ("h2", "10. Contato"),
        ("p", "Dúvidas sobre esta política ou sobre o aplicativo: "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a>"),
        ("p", "Desenvolvedor: <strong>wanggit</strong> (desenvolvedor individual), publicador de "
              "<em>Numeria: Calculadoras financeiras</em> na App Store."),
    ],
    "disclaimer_head": "Não é aconselhamento financeiro",
    "disclaimer": "A Numeria produz estimativas aritméticas para fins de planejamento. Seus "
                  "resultados não constituem aconselhamento financeiro, tributário, jurídico ou de "
                  "investimento, e não levam em conta todas as suas circunstâncias. Consulte um "
                  "profissional qualificado antes de agir com base em qualquer número que o "
                  "aplicativo mostrar.",
}

FR = {
    "code": "fr",
    "html_lang": "fr",
    "label": "Français",
    "dir": "ltr",
    "doc_title": "Numeria — Politique de confidentialité",
    "h1": "Politique de confidentialité",
    "product": "<strong>Numeria : Calculateurs financiers</strong> &middot; version 1.0.0 &middot; iOS (iPhone)",
    "effective": "Date d&rsquo;entrée en vigueur : 13 septembre 2026",
    "tldr_head": "En une phrase",
    "tldr": "Numeria ne collecte rien. Pas de compte, pas de publicité, pas d&rsquo;analyse "
            "d&rsquo;audience, pas de serveur : chaque calcul s&rsquo;effectue intégralement sur "
            "votre appareil, et les chiffres que vous saisissez ne sont jamais enregistrés ni transmis.",
    "blocks": [
        ("h2", "1. Ce que nous ne collectons pas"),
        ("p", "Numeria ne comporte aucun composant serveur et l&rsquo;application n&rsquo;émet "
              "aucune requête réseau qui lui soit propre. Nous ne pouvons donc pas collecter — et "
              "n&rsquo;avons jamais collecté — les éléments suivants :"),
        ("ul", [
            "les identifiants personnels tels que votre nom, adresse e-mail, numéro de téléphone ou date de naissance",
            "les informations de comptes financiers telles que les numéros de compte bancaire, de carte ou de courtage",
            "la localisation précise ou approximative",
            "les contacts, photos, données de santé ou tout autre contenu de votre appareil",
            "les analyses d&rsquo;utilisation, les profils comportementaux ou l&rsquo;identifiant publicitaire (IDFA)",
        ]),
        ("p", "Puisque rien n&rsquo;est collecté en premier lieu, il n&rsquo;existe rien qui puisse "
              "être partagé avec un tiers, vendu, ou exposé lors d&rsquo;une fuite de données. "
              "L&rsquo;étiquette de confidentialité de Numeria sur l&rsquo;App Store est "
              "<strong>« Données non collectées » (Data Not Collected)</strong>."),

        ("h2", "2. Ce qui est conservé sur votre appareil"),
        ("p", "Numeria écrit une petite quantité de données dans le stockage local des préférences "
              "de votre appareil afin de mémoriser vos choix d&rsquo;un lancement à l&rsquo;autre. "
              "Ces données ne quittent jamais votre appareil et ne nous sont pas lisibles :"),
        ("table", {
            "head": ["Donnée conservée", "Sa raison d&rsquo;être"],
            "rows": [
                ["Les identifiants des 10 derniers calculateurs ouverts",
                 "Alimentent la liste « Récents » sur l&rsquo;écran d&rsquo;accueil"],
                ["Les identifiants des calculateurs marqués comme favoris",
                 "Alimentent votre liste « Favoris »"],
                ["La préférence de symbole monétaire",
                 "Formate les montants comme vous le souhaitez"],
                ["La préférence de thème (clair, sombre ou système)",
                 "Applique l&rsquo;apparence que vous avez choisie"],
                ["La préférence de langue",
                 "Affiche l&rsquo;interface dans votre langue"],
                ["Le marqueur de déverrouillage",
                 "Mémorise votre achat « Tout déverrouiller » pour ne jamais vous le faire payer deux fois"],
            ],
        }),
        ("note", "<strong>Les chiffres que vous saisissez ne sont pas enregistrés.</strong> Aucune "
                 "saisie, valeur intermédiaire ou résultat de calculateur n&rsquo;est écrit sur le "
                 "disque ni envoyé où que ce soit. Fermer un calculateur efface ce que vous y aviez saisi."),

        ("h2", "3. Achats"),
        ("p", "Numeria propose un unique achat intégré non consommable, « Déverrouiller tous les "
              "calculateurs ». Le paiement est traité intégralement par Apple via l&rsquo;App Store "
              "et StoreKit. Nous ne voyons, ne recevons ni ne conservons jamais votre moyen de "
              "paiement, votre numéro de carte, votre identifiant Apple ou votre historique d&rsquo;achats."),
        ("p", "La seule donnée liée à l&rsquo;achat que l&rsquo;application conserve est le "
              "marqueur local de déverrouillage décrit ci-dessus. Lorsque vous utilisez "
              "<em>Restaurer les achats</em>, l&rsquo;application interroge l&rsquo;App Store "
              "directement depuis votre appareil ; la réponse sert uniquement à positionner ce "
              "marqueur et ne nous est pas transmise. Les remboursements sont gérés par Apple "
              "selon ses propres conditions."),

        ("h2", "4. Tiers"),
        ("p", "Numeria n&rsquo;intègre aucun SDK tiers — ni régie publicitaire, ni fournisseur "
              "d&rsquo;analyse d&rsquo;audience, ni SDK de réseau social, ni outil de rapport "
              "d&rsquo;incident. Les seuls services de plateforme avec lesquels il communique sont :"),
        ("ul", [
            "l&rsquo;App Store d&rsquo;Apple, uniquement pour valider l&rsquo;achat intégré, et",
            "le navigateur externe de votre appareil, lorsque vous touchez les liens "
            "<em>Assistance</em> ou <em>Politique de confidentialité</em> dans les Réglages et que "
            "le système ouvre cette URL en dehors de l&rsquo;application.",
        ]),

        ("h2", "5. À propos de cette page web"),
        ("p", "L&rsquo;application ne collecte rien, mais ce document est hébergé sur GitHub Pages "
              "afin que l&rsquo;App Store dispose d&rsquo;une URL à laquelle renvoyer. Lorsque vous "
              "la chargez, GitHub peut enregistrer les informations de journalisation serveur "
              "standards — telles que votre adresse IP, le type de navigateur et l&rsquo;heure de "
              "la requête — conformément à la "
              "<a href=\"" + _GH + "\" rel=\"noopener\">propre déclaration de confidentialité de GitHub</a>. "
              "Nous ne recevons pas ces journaux et n&rsquo;y avons pas accès."),
        ("p", "Cette page ne charge aucune police, aucun script, aucune feuille de style, aucune "
              "image ni aucun traceur externe. La seule chose qu&rsquo;elle écrit dans votre "
              "navigateur est la langue que vous avez choisie, afin que la page s&rsquo;ouvre dans "
              "cette même langue la prochaine fois."),

        ("h2", "6. Enfants"),
        ("p", "Numeria est un outil de calcul généraliste classé 4+. Il ne s&rsquo;adresse pas aux "
              "enfants et ne collecte de données auprès de personne, enfants compris."),

        ("h2", "7. Conservation et suppression des données"),
        ("p", "Il n&rsquo;existe aucune copie de vos données côté serveur : nous n&rsquo;avons donc "
              "rien à conserver, exporter ou supprimer. Pour effacer toute trace des données "
              "écrites par Numeria, supprimez simplement l&rsquo;application : la désinstallation "
              "efface les préférences locales énumérées à la section 2."),

        ("h2", "8. Vos droits"),
        ("p", "Comme Numeria ne détient aucune donnée personnelle vous concernant, il n&rsquo;y a "
              "aucune donnée personnelle que nous puissions divulguer, rectifier, exporter ou "
              "effacer à votre demande. Les droits garantis par le RGPD, le CCPA et les "
              "réglementations similaires portent sur des données personnelles, et cette "
              "application n&rsquo;en crée aucune. Si vous estimez qu&rsquo;un élément de cette "
              "page est inexact, signalez-le-nous et nous le corrigerons."),

        ("h2", "9. Modifications de cette politique"),
        ("p", "Si une version future de Numeria modifie quoi que ce soit décrit ici — par exemple "
              "l&rsquo;ajout d&rsquo;une synchronisation facultative dans le cloud ou de toute "
              "fonctionnalité réseau — nous mettrons cette page à jour, réviserons la date "
              "d&rsquo;entrée en vigueur ci-dessus et annoncerons le changement dans les notes de "
              "version de l&rsquo;App Store avant la publication de cette version."),

        ("h2", "10. Contact"),
        ("p", "Pour toute question sur cette politique ou sur l&rsquo;application : "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a>"),
        ("p", "Développeur : <strong>wanggit</strong> (développeur individuel), éditeur de "
              "<em>Numeria : Calculateurs financiers</em> sur l&rsquo;App Store."),
    ],
    "disclaimer_head": "Ceci n&rsquo;est pas un conseil financier",
    "disclaimer": "Numeria produit des estimations arithmétiques destinées à la planification. Ses "
                  "résultats ne constituent pas un conseil financier, fiscal, juridique ou en "
                  "investissement, et ne tiennent pas compte de l&rsquo;ensemble de votre "
                  "situation. Consultez un professionnel qualifié avant d&rsquo;agir sur la base "
                  "d&rsquo;un chiffre affiché par l&rsquo;application.",
}

DE = {
    "code": "de",
    "html_lang": "de",
    "label": "Deutsch",
    "dir": "ltr",
    "doc_title": "Numeria — Datenschutzerklärung",
    "h1": "Datenschutzerklärung",
    "product": "<strong>Numeria: Finanzrechner</strong> &middot; Version 1.0.0 &middot; iOS (iPhone)",
    "effective": "Stand: 13. September 2026",
    "tldr_head": "In einem Satz",
    "tldr": "Numeria erhebt nichts. Kein Konto, keine Werbung, kein Tracking und kein Server — "
            "jede Berechnung läuft vollständig auf Ihrem Gerät, und die eingegebenen Zahlen werden "
            "weder gespeichert noch übertragen.",
    "blocks": [
        ("h2", "1. Was wir nicht erheben"),
        ("p", "Numeria hat keine Serverkomponente und die App stellt selbst keine Netzwerkanfragen. "
              "Deshalb können wir Folgendes nicht erheben — und haben es auch nie getan:"),
        ("ul", [
            "personenbezogene Merkmale wie Name, E-Mail-Adresse, Telefonnummer oder Geburtsdatum",
            "Finanzkontodaten wie Bank-, Karten- oder Depotnummern",
            "genauen oder ungefähren Standort",
            "Kontakte, Fotos, Gesundheitsdaten oder sonstige Inhalte Ihres Geräts",
            "Nutzungsanalysen, Verhaltensprofile oder die Werbekennung (IDFA)",
        ]),
        ("p", "Weil von vornherein nichts erhoben wird, gibt es auch nichts, das an Dritte "
              "weitergegeben, verkauft oder durch eine Datenpanne offengelegt werden könnte. Die "
              "Datenschutzkennzeichnung von Numeria im App Store lautet "
              "<strong>„Keine Datenerhebung“ (Data Not Collected)</strong>."),

        ("h2", "2. Was auf Ihrem Gerät gespeichert wird"),
        ("p", "Numeria schreibt eine kleine Menge Daten in den lokalen Einstellungsspeicher Ihres "
              "Geräts, um Ihre Entscheidungen zwischen den Starts zu behalten. Diese Daten "
              "verlassen Ihr Gerät nie und sind für uns nicht lesbar:"),
        ("table", {
            "head": ["Gespeicherter Eintrag", "Zweck"],
            "rows": [
                ["Kennungen der letzten 10 geöffneten Rechner",
                 "Füllen die Liste „Zuletzt verwendet“ auf dem Startbildschirm"],
                ["Kennungen der als Favorit markierten Rechner",
                 "Füllen Ihre „Favoriten“-Liste"],
                ["Währungssymbol-Einstellung",
                 "Formatiert Geldbeträge so, wie Sie es erwarten"],
                ["Design-Einstellung (hell, dunkel oder System)",
                 "Wendet das gewählte Erscheinungsbild an"],
                ["Spracheinstellung",
                 "Zeigt die Oberfläche in Ihrer Sprache an"],
                ["Freischalt-Markierung",
                 "Merkt sich Ihren Kauf „Alle freischalten“, damit Sie nie zweimal zahlen"],
            ],
        }),
        ("note", "<strong>Ihre Eingabezahlen werden nicht gespeichert.</strong> Keine "
                 "Rechnereingabe, kein Zwischenwert und kein Ergebnis wird auf die Festplatte "
                 "geschrieben oder irgendwohin gesendet. Beim Schließen eines Rechners werden Ihre "
                 "Eingaben verworfen."),

        ("h2", "3. Käufe"),
        ("p", "Numeria bietet genau einen nicht verbrauchbaren In-App-Kauf an: „Alle Rechner "
              "freischalten“. Die Zahlung wird vollständig von Apple über den App Store und "
              "StoreKit abgewickelt. Wir sehen, erhalten oder speichern niemals Ihre "
              "Zahlungsmethode, Kartennummer, Apple-ID oder Kaufhistorie."),
        ("p", "Die einzige kaufbezogene Angabe, die die App behält, ist die oben beschriebene "
              "lokale Freischalt-Markierung. Wenn Sie <em>Käufe wiederherstellen</em> nutzen, "
              "fragt die App den App Store direkt von Ihrem Gerät aus ab; die Antwort wird nur zum "
              "Setzen dieser Markierung verwendet und nicht an uns weitergeleitet. Erstattungen "
              "richtet Apple nach seinen eigenen Bedingungen."),

        ("h2", "4. Dritte"),
        ("p", "Numeria bindet keine SDKs Dritter ein — keine Werbenetzwerke, keine "
              "Analysedienste, keine Social-Media-SDKs, keine Crash-Reporter. Die einzigen "
              "Plattformdienste, mit denen die App kommuniziert, sind:"),
        ("ul", [
            "Apples App Store, ausschließlich zur Prüfung des In-App-Kaufs, und",
            "der externe Browser Ihres Geräts, wenn Sie in den Einstellungen auf <em>Support</em> "
            "oder <em>Datenschutzerklärung</em> tippen und das System diese URL außerhalb der App öffnet.",
        ]),

        ("h2", "5. Über diese Webseite"),
        ("p", "Die App erhebt nichts, aber dieses Dokument wird auf GitHub Pages gehostet, damit "
              "der App Store eine verlinkbare URL hat. Beim Laden kann GitHub übliche "
              "Serverprotokolldaten erfassen — etwa Ihre IP-Adresse, den Browsertyp und die "
              "Anfragezeit — gemäß der "
              "<a href=\"" + _GH + "\" rel=\"noopener\">eigenen Datenschutzerklärung von GitHub</a>. "
              "Wir erhalten diese Protokolle nicht und haben keinen Zugriff darauf."),
        ("p", "Diese Seite lädt keine externen Schriften, Skripte, Stylesheets, Bilder oder "
              "Tracker. Das Einzige, was sie in Ihrem Browser ablegt, ist die von Ihnen gewählte "
              "Sprache, damit die Seite beim nächsten Mal in derselben Sprache öffnet."),

        ("h2", "6. Kinder"),
        ("p", "Numeria ist ein allgemeines Berechnungswerkzeug mit einer Altersfreigabe von 4+. Es "
              "richtet sich nicht an Kinder und erhebt keinerlei Daten — auch nicht von Kindern."),

        ("h2", "7. Speicherung und Löschung von Daten"),
        ("p", "Es gibt keine serverseitige Kopie Ihrer Daten, also haben wir nichts zu speichern, "
              "zu exportieren oder zu löschen. Um jede Spur der von Numeria geschriebenen Daten zu "
              "entfernen, löschen Sie einfach die App: Die Deinstallation löscht die in Abschnitt 2 "
              "aufgeführten lokalen Einstellungen."),

        ("h2", "8. Ihre Rechte"),
        ("p", "Da Numeria keine personenbezogenen Daten über Sie besitzt, gibt es keine "
              "personenbezogenen Daten, die wir auf Anfrage offenlegen, berichtigen, exportieren "
              "oder löschen könnten. Die Rechte aus DSGVO, CCPA und ähnlichen Regelungen knüpfen an "
              "personenbezogene Daten an, und diese App erzeugt keine. Falls Sie eine Angabe auf "
              "dieser Seite für unzutreffend halten, teilen Sie uns das bitte mit — wir korrigieren sie."),

        ("h2", "9. Änderungen dieser Erklärung"),
        ("p", "Sollte eine künftige Version von Numeria etwas an den hier beschriebenen Umständen "
              "ändern — etwa durch eine optionale Cloud-Synchronisation oder irgendeine "
              "Netzwerkfunktion —, aktualisieren wir diese Seite, passen das oben genannte "
              "Datum an und weisen vor der Veröffentlichung jener Version in den App-Store-"
              "Versionshinweisen darauf hin."),

        ("h2", "10. Kontakt"),
        ("p", "Fragen zu dieser Erklärung oder zur App: "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a>"),
        ("p", "Entwickler: <strong>wanggit</strong> (Einzelentwickler), Anbieter von "
              "<em>Numeria: Finanzrechner</em> im App Store."),
    ],
    "disclaimer_head": "Keine Finanzberatung",
    "disclaimer": "Numeria erzeugt arithmetische Schätzwerte für Planungszwecke. Die Ausgaben sind "
                  "keine Finanz-, Steuer-, Rechts- oder Anlageberatung und berücksichtigen Ihre "
                  "gesamte Situation nicht. Ziehen Sie eine qualifizierte Fachperson hinzu, bevor "
                  "Sie aufgrund einer von der App angezeigten Zahl handeln.",
}

HI = {
    "code": "hi",
    "html_lang": "hi",
    "label": "हिन्दी",
    "dir": "ltr",
    "doc_title": "Numeria — गोपनीयता नीति",
    "h1": "गोपनीयता नीति",
    "product": "<strong>Numeria: वित्त कैलकुलेटर</strong> &middot; संस्करण 1.0.0 &middot; iOS (iPhone)",
    "effective": "प्रभावी तिथि: 13 सितंबर 2026",
    "tldr_head": "एक वाक्य में",
    "tldr": "Numeria कुछ भी एकत्र नहीं करता। न खाता, न विज्ञापन, न एनालिटिक्स, न सर्वर — "
            "हर गणना पूरी तरह आपके डिवाइस पर होती है, और आपके द्वारा डाले गए अंक न तो सहेजे "
            "जाते हैं, न भेजे जाते हैं।",
    "blocks": [
        ("h2", "1. हम क्या एकत्र नहीं करते"),
        ("p", "Numeria में कोई सर्वर घटक नहीं है और ऐप स्वयं कोई नेटवर्क अनुरोध नहीं भेजता। "
              "इसलिए हम निम्नलिखित एकत्र नहीं कर सकते — और कभी किए भी नहीं:"),
        ("ul", [
            "नाम, ईमेल पता, फ़ोन नंबर या जन्म तिथि जैसे व्यक्तिगत पहचानकर्ता",
            "बैंक, कार्ड या ब्रोकरेज खाता संख्याओं जैसी वित्तीय खाता जानकारी",
            "सटीक या अनुमानित स्थान",
            "संपर्क, फ़ोटो, स्वास्थ्य डेटा, या आपके डिवाइस की कोई अन्य सामग्री",
            "उपयोग एनालिटिक्स, व्यवहार प्रोफ़ाइल, या विज्ञापन पहचानकर्ता (IDFA)",
        ]),
        ("p", "चूँकि शुरू में ही कुछ एकत्र नहीं होता, इसलिए कोई ऐसी चीज़ नहीं है जिसे किसी तृतीय "
              "पक्ष के साथ साझा या बेचा जा सके, या जो लीक हो सके। App Store पर Numeria का "
              "गोपनीयता लेबल <strong>「Data Not Collected」(डेटा एकत्र नहीं किया जाता)</strong> है।"),

        ("h2", "2. आपके डिवाइस पर क्या सहेजा जाता है"),
        ("p", "ताकि ऐप आपके चुनाव याद रख सके, Numeria आपके डिवाइस के स्थानीय प्राथमिकता संग्रह "
              "में थोड़ा डेटा लिखता है। यह डेटा कभी आपके डिवाइस से बाहर नहीं जाता और हम उसे "
              "पढ़ नहीं सकते:"),
        ("table", {
            "head": ["सहेजा गया आइटम", "उसका प्रयोजन"],
            "rows": [
                ["आपके खोले गए अंतिम 10 कैलकुलेटरों की पहचान",
                 "होम स्क्रीन पर 「हाल के」 की सूची भरने के लिए"],
                ["पसंदीदा के रूप में चिह्नित कैलकुलेटरों की पहचान",
                 "आपकी 「पसंदीदा」 सूची भरने के लिए"],
                ["मुद्रा चिह्न प्राथमिकता",
                 "राशियों को आपकी अपेक्षा अनुसार प्रदर्शित करने के लिए"],
                ["थीम प्राथमिकता (लाइट, डार्क या सिस्टम)",
                 "आपकी चुनी हुई रूपरेखा लागू करने के लिए"],
                ["भाषा प्राथमिकता",
                 "इंटरफ़ेस आपकी भाषा में दिखाने के लिए"],
                ["अनलॉक फ़्लैग",
                 "याद रखने के लिए कि आपने 「सभी अनलॉक」 खरीदा है, ताकि दोबारा भुगतान न माँगा जाए"],
            ],
        }),
        ("note", "<strong>आपके डाले गए अंक सहेजे नहीं जाते।</strong> न कोई कैलकुलेटर इनपुट, न "
                 "मध्यवर्ती मान, न परिणाम डिस्क पर लिखा जाता है या कहीं भेजा जाता है। कैलकुलेटर "
                 "बंद करते ही आपने उसमें जो टाइप किया वह हट जाता है।"),

        ("h2", "3. खरीद"),
        ("p", "Numeria केवल एक गैर-उपभोज्य इन-ऐप खरीद प्रदान करता है — 「सभी कैलकुलेटर अनलॉक "
              "करें」। भुगतान पूरी तरह Apple द्वारा App Store और StoreKit के ज़रिए संसाधित होता "
              "है। हम आपका भुगतान साधन, कार्ड नंबर, Apple ID या खरीद इतिहास कभी नहीं देखते, "
              "प्राप्त नहीं करते, न सहेजते हैं।"),
        ("p", "खरीद से संबंधित एकमात्र डेटा जो ऐप रखता है वह ऊपर बताया गया स्थानीय अनलॉक फ़्लैग "
              "है। जब आप <em>खरीद बहाल करें</em> का उपयोग करते हैं, तो ऐप सीधे आपके डिवाइस से "
              "App Store से पूछता है; उसका उत्तर केवल वही फ़्लैग सेट करने में उपयोग होता है और "
              "हमें अग्रेषित नहीं किया जाता। धनवापसी Apple अपनी नीतियों के अनुसार संभालता है।"),

        ("h2", "4. तृतीय पक्ष"),
        ("p", "Numeria में कोई तृतीय-पक्ष SDK नहीं है — न विज्ञापन नेटवर्क, न एनालिटिक्स प्रदाता, "
              "न सोशल मीडिया SDK, न क्रैश रिपोर्टर। यह केवल इन प्लेटफ़ॉर्म सेवाओं से बात करता है:"),
        ("ul", [
            "Apple का App Store — केवल इन-ऐप खरीद सत्यापित करने के लिए, और",
            "आपके डिवाइस का बाहरी ब्राउज़र — जब आप सेटिंग्स में <em>सहायता</em> या "
            "<em>गोपनीयता नीति</em> लिंक दबाते हैं तो सिस्टम वह URL ऐप के बाहर खोल देता है।",
        ]),

        ("h2", "5. इस वेब पृष्ठ के बारे में"),
        ("p", "ऐप कुछ भी एकत्र नहीं करता, पर यह दस्तावेज़ GitHub Pages पर होस्ट किया गया है ताकि "
              "App Store के पास जोड़ने हेतु कोई URL हो। इसे लोड करने पर GitHub मानक सर्वर लॉग "
              "जानकारी दर्ज कर सकता है — जैसे आपका IP पता, ब्राउज़र प्रकार और अनुरोध समय — "
              "<a href=\"" + _GH + "\" rel=\"noopener\">GitHub की अपनी गोपनीयता नीति</a> के "
              "अनुसार। हमें वे लॉग नहीं मिलते और न ही उनकी पहुँच है।"),
        ("p", "यह पृष्ठ कोई बाहरी फ़ॉन्ट, स्क्रिप्ट, स्टाइलशीट, छवि या ट्रैकर लोड नहीं करता। "
              "यह आपके ब्राउज़र में केवल आपकी चुनी हुई भाषा लिखता है, ताकि अगली बार पृष्ठ उसी "
              "भाषा में खुले।"),

        ("h2", "6. बच्चे"),
        ("p", "Numeria एक सामान्य-उपयोग गणना उपकरण है जिसकी आयु श्रेणी 4+ है। यह बच्चों के लिए "
              "नहीं बनाया गया और यह किसी से भी — बच्चों सहित — कोई डेटा एकत्र नहीं करता।"),

        ("h2", "7. डेटा प्रतिधारण और विलोपन"),
        ("p", "आपके डेटा की कोई सर्वर-पक्ष प्रतिलिपि नहीं है, इसलिए हमारे पास रखने, निर्यात करने "
              "या मिटाने के लिए कुछ नहीं है। Numeria द्वारा लिखे गए हर निशान को हटाने के लिए "
              "बस ऐप हटा दें: अनइंस्टॉल करने से खंड 2 में सूचीबित स्थानीय प्राथमिकताएँ मिट जाती हैं।"),

        ("h2", "8. आपके अधिकार"),
        ("p", "चूँकि Numeria आपके बारे में कोई व्यक्तिगत डेटा नहीं रखता, इसलिए अनुरोध पर "
              "प्रकट करने, सुधारने, निर्यात करने या मिटाने हेतु कोई व्यक्तिगत डेटा है ही नहीं। "
              "GDPR, CCPA और ऐसे ही नियमों के अंतर्गत अधिकार व्यक्तिगत डेटा से जुड़े होते हैं, "
              "और यह ऐप कोई व्यक्तिगत डेटा बनाता नहीं। यदि आपको लगता है कि इस पृष्ठ की कोई बात "
              "ग़लत है, कृपया बताएँ — हम सुधार देंगे।"),

        ("h2", "9. इस नीति में बदलाव"),
        ("p", "यदि Numeria का भविष्य का कोई संस्करण यहाँ बताई किसी बात को बदलता है — मिसाल के "
              "तौर पर, यदि हम वैकल्पिक क्लाउड सिंक या कोई नेटवर्क सुविधा जोड़ें — तो हम इस पृष्ठ "
              "को अद्यतन करेंगे, ऊपर की प्रभावी तिथि सुधारेंगे, और उस संस्करण के जारी होने से पहले "
              "App Store के रिलीज़ नोट्स में बदलाव बताएँगे।"),

        ("h2", "10. संपर्क"),
        ("p", "इस नीति या ऐप के बारे में प्रश्न: "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a>"),
        ("p", "डेवलपर: <strong>wanggit</strong> (व्यक्तिगत डेवलपर), App Store पर "
              "<em>Numeria: वित्त कैलकुलेटर</em> के प्रकाशक।"),
    ],
    "disclaimer_head": "यह वित्तीय सलाह नहीं है",
    "disclaimer": "Numeria योजना बनाने के लिए अंकगणितीय अनुमान देता है। इसका परिणाम वित्तीय, कर, "
                  "क़ानूनी या निवेश सलाह नहीं है, और यह आपकी पूरी परिस्थितियों को ध्यान में नहीं "
                  "रखता। ऐप द्वारा दिखाए गए किसी भी अंक पर काम करने से पहले किसी योग्य पेशेवर से "
                  "सलाह लें।",
}
