WSpZ
====

Dies ist der Quelltext der inoffiziellen Website des Wassersportzentrums der FAU Erlangen-Nürnberg.

Das System wurde mit Hilfe von [Lektor CMS](https://www.getlektor.com/) realisiert.

Änderungen
----------

Einfach ein [Ticket anlegen und dort den Änderungswunsch angeben](https://github.com/nils-werner/wspz/issues/new?title=Vorschlag%20fuer%20/wiki/contents.lr).

Roadmap
-------

Die Seite in ihrer jetzigen Form ist auf einem möglist kleinen Wartungs-Aufwand ausgelegt. Die Pflege der Seiten ist daher, vor allem für Neulinge, nicht sehr benutzerfreundlich.

Sollte die Anzahl der Beiträge und Änderungen dritter groß genug und der Wunsch nach einfacherer Webseiten-Pflege laut werden, kann ein Wechsel auf ein komplett online-basiertes CMS wie [Craft](https://craftcms.com/) oder [Wagtail](https://wagtail.io/) durchgeführt werden.

Installation
------------

Zur lokalen Installation der Website benötigst du folgende Software:

 - Node
 - npm
 - Python
 - pip

Installation:

    pip install -r requirements.txt
    lektor server -f webpack

Danach kann die Website auf

    http://localhost:5000

aufgerufen werden.
