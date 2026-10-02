---
name: registre-de-demarche
description: Tenir la mémoire d'une démarche de travail longue de Laurent Cieutat — ce qui a été affirmé, ce qui a été renversé et par quoi, ce qui a été décidé, les désaccords, les murs, et le lexique des notions inventées en route. Se déclenche quand Laurent clôt une vague ou une session de travail, quand un agent rend un retour qui renverse une affirmation antérieure, quand il demande d'acter, de verser au registre ou de valider en mémoire la démarche, et quand une session neuve doit reprendre un projet existant. Interdit d'effacer une assertion fausse : on la marque renversée et par quoi. Refuse d'écrire une ligne sans son couple de preuve.
---

# Registre de démarche

## Pourquoi cette compétence existe

Une démarche longue produit trois choses qu'aucun livrable ne garde : **ce qui a été cru puis détruit**, **le vocabulaire inventé en route**, et **ce qui a bloqué**. Sans elles, une session neuve recommence les mêmes erreurs, ne comprend plus les fichiers, et redécouvre les mêmes murs.

Claude n'a aucune mémoire d'une session à l'autre. Le registre est la mémoire, et il vit dehors.

## La règle qui fonde tout

**Une assertion renversée n'est jamais effacée. Elle est marquée renversée, et par quoi.**

Ce qui a été cru puis détruit vaut plus que la seule conclusion, parce que c'est la seule chose qui empêche de le recroire. Un registre qui ne garde que les conclusions justes est un registre qui mentira dans six mois.

## Où écrire

`REGISTRE-DE-DEMARCHE.md`, à la racine du projet. Un seul fichier, jamais découpé — c'est la première chose qu'une session neuve ouvre, avant les livrables et avant les critiques.

Si le projet vit dans Notion, le registre y est dupliqué par la page du projet. Le fichier reste la source, Notion reste la vitrine.

## Les sept registres

Dans cet ordre, parce qu'il va du plus durable au plus volatil.

| Registre | Ce qu'il porte | Ce qu'il empêche |
|---|---|---|
| **1 Lexique** | Les notions inventées en séance, avec ce qu'elles désignent et de quoi elles sont nées | Qu'une session neuve ouvre les fichiers sans rien comprendre |
| **2 Assertions renversées** | Chaque affirmation tombée, son auteur, ce qui l'a renversée, et le couple de preuve du renversement | De recroire demain ce qui est tombé aujourd'hui |
| **3 Faits qui tiennent** | Les faits établis, chacun avec son couple de preuve et sa source | De confondre ce qui est mesuré et ce qui est supposé |
| **4 Décisions** | Ce que Laurent a tranché, sur quelles assertions, et l'état de validité de ce fondement | Qu'une décision prise sous incertitude devienne un acquis par oubli |
| **5 Désaccords** | Quand Claude a objecté et que Laurent a tranché autrement, avec **ce qui dira plus tard qui avait raison** | De ne jamais savoir qui avait raison, donc de mal régler la confiance |
| **6 Murs** | Hôtes refusés, sources inaccessibles, documents non lus, trous de preuve assumés, limites de méthode établies | Qu'un trou connu soit redécouvert à chaque session |
| **7 En attente** | Ce qui attend une décision ou une dépense, avec ce que ça débloque | Qu'une action gratuite et décisive dorme pendant des semaines |

Le lexique est en premier et c'est celui qu'on oublie. Une démarche sérieuse invente une dizaine de notions en quelques heures, et aucune n'existe ailleurs.

## Le couple de preuve — provenance et robustesse

Toute ligne du registre porte un couple, jamais une lettre seule. Deux axes, parce que « d'où vient l'information » et « à quel point elle est solide » sont deux questions distinctes, et les confondre verrouille tout raisonnement.

**Provenance, en lettres** — `A` mesuré, commande et sortie collées · `B` source primaire, URL et date de consultation · `C` source secondaire · `D` mémoire du modèle, sans vérification.

**Robustesse, en chiffres** — `1` rejouable par un tiers · `2` attesté, mais le chemin ne se refait plus · `3` étroit, échantillon ou date ou corpus manquants · `4` non étayé.

Une ligne s'écrit `B·2`. Lecture : **1 et 2 portent** une décision, **3 est indicatif**, **4 va au dépôt**.

Deux conséquences à ne pas adoucir : **`C·1` vaut plus que `A·3`**, et c'est voulu. **`D·1` n'existe pas.** `A·4` est rejeté, pas rangé.

Une variante admise, et une seule : **`1†`**, rejouable par un tiers admis au périmètre, le titulaire d'un mandat compris. Commercialement, l'opposabilité devant le client vaut mieux que la reproductibilité publique.

## Ce que cette compétence refuse

— **Écrire une ligne sans son couple.** Une affirmation sans couple est une opinion déguisée en registre
— **Effacer une assertion renversée.** Elle descend au registre 2, elle ne disparaît pas
— **Inscrire une décision sans dire sur quelles assertions elle repose.** Sinon on ne saura jamais qu'elle a perdu son fondement
— **Inscrire un désaccord sans dire ce qui dira plus tard qui avait raison.** Un désaccord sans juge futur est un ressentiment, pas un registre
— **Convertir un effort en jours sans l'avoir chronométré.** Un budget inventé est du cran D déguisé en chiffre
— **Oublier le lexique**, qui est le registre le moins spectaculaire et le plus décisif

## Le geste, pas à pas

1. **Lire le registre existant en entier.** Jamais écrire par-dessus sans avoir lu : le registre 2 dit ce qui est déjà tombé
2. **Trier le nouveau matériau** — ce qui renverse une ligne existante, ce qui est un fait neuf, ce qui est une décision, un désaccord, un mur
3. **Pour chaque renversement** : déplacer l'assertion du registre 3 vers le registre 2, en nommant qui l'a renversée, par quoi, et avec quel couple. Ne jamais la supprimer du fichier
4. **Pour chaque notion neuve** : l'inscrire au lexique avec ce dont elle est née. Une notion sans origine sera réinventée différemment
5. **Relire le registre 4** : une décision dont le fondement vient d'être renversé change d'état. Le dire, sans réclamer qu'elle soit changée — c'est Laurent qui décide
6. **Relire le registre 7** : ce qui est devenu gratuit ou décisif remonte en tête
7. **Écrire, committer, pousser.** Un registre qui vit dans un conteneur éphémère n'a pas eu lieu

## Quand déclencher sans qu'on le demande

— Un agent rend un retour qui contredit une ligne du registre 3
— Laurent tranche un arbitrage, surtout contre un avis donné
— Un hôte, une source ou un document se révèle inaccessible
— Une notion est inventée en séance et réutilisée une deuxième fois
— Une erreur relayée comme un fait est découverte : c'est le cas le plus urgent, et c'est là que le registre se gagne ou se perd

## Ce que cette compétence n'est pas

Ce n'est pas un journal de bord, pas un compte rendu, pas une liste de tâches. Un journal raconte ce qui s'est passé ; le registre dit **ce qui est vrai, ce qui est tombé, et avec quelle force**.

Et ce n'est pas un instrument de conformité : il ne sert pas à prouver qu'on a bien travaillé. Il sert à ce qu'une session neuve reprenne en une lecture ce qui a coûté des heures à établir.
