# Semestrální práce - Analýza území {: .page_title}

## Zadání
Nad zadaným územím proveďte následující analýzy s využitím GIS softwaru. Výsledky jednotlivých úloh následně publikujte formou webové mapové aplikace na ArcGIS Online či pomocí open-source řešení (např. GISQuick). Tato aplikace může mít libovolnou formu, takovou, kterou uznáte za vhodnou či zajímavou (ArcGIS Instant Apps, Story Maps, Experience Builder,...). 

Svou aplikaci na konci semestru krátce odprezentujete před ostatními v 5 minutové prezentaci. 

Dotazy či připomínky k semestrální práci směřujte sem: *frantisek.muzik@fsv.cvut.cz*

<div class="grid cards" markdown>

-   :simple-maildotru: __Konkrétní zadání__ 
    
    ---

    Bude rozesláno každému emailem.

-   :material-presentation-play: __Termín prezentace__
    
    ---

    __7.5.2025__ proběhne __5 minutová__ prezentace výsledné online webové mapové aplikace.
</div>

<hr class="level-1">

**Pro zadané území vypracujte následující úkoly:**

### 1. Identifikace obce a katastrálních území

- Zjistěte v jaké obci se nachází zadaný definiční bod. Import Excelu s body můžete provést např. funkcí XY Table to Point. Následně si vyexportujte váš zadaný bod do samostatné vrstvy.

- Vyberte odpovídající obec z databáze [RÚIAN](https://k155cvut.github.io/gis-1/data/#ruian) a exportujte ji jako samostatnou vrstvu.

- Dále zjistěte jaká katastrální území se nachází na území vaší obce a v jakém z nich leží zadaný bod. Všechna katastrální území spadající do obce také z RÚIANu vyexportujte do samosatné vrstvy.

### 2. Adresní místa

- Určete počet adresních míst na území dané obce (zdroj: RÚIAN). Adresní místa zobrazte v mapě.

- Vyberte stavební objekty v obci (zdroj: RÚIAN). Tyto objekty vhodně vizualizujte dle připojení na Připojení na rozvod plynu.

|KÓD| Připojení na rozvod plynu               |
|---|----------------------|
| 1 |Plyn z veřejné sítě   |
| 2 |Plyn z dom. zásobníku |
| 3 |Bez plynu             |
| 8 |Nedefinováno          |
| 9 |Nezjištěno            |
| 51|Plyn v domě           |

### 3. Chráněná území v okolí obce

- Zjistěte, zda se na území zadané obce a v 10 km kolem ní nachází celou plochou maloplošné zvláště chráněné území (zdroj: ZABAGED). 

- Pokud ano, zobrazte jej v mapě jako samostatnou vrstvu. Zobrazte názvy vybraných území (záložka Labeling -> Field: NAZEV)

### 4. Vytvoření vrstvy využití pozemků

- Vytvořte samostatnou vrstvu, která bude obsahovat data způsobu využití pozemku **pro kružnici o poloměru 700 metrů kolem zadaného bodu** (zdroj: RÚIAN – vrstva *Parcela*). Pro urychlení výpočtu nejprve vyberte parcely na základě atributu *Nadřazené katastrální území*.

- Dle atributů v tabulce níže vypočítejte pro data nový sloupec *TYP_VYUZITI*, na základě kterého vrstvu následně vhodně vizualizujte. Číselníky pro přiřazení kódů: [Způsob využití pozemku](https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Ciselniky-ISKN/Ciselniky-k-nemovitosti/Zpusob-vyuziti-pozemku.aspx), [Kód druhu pozemku](https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Ciselniky-ISKN/Ciselniky-k-nemovitosti/Druh-pozemku.aspx). Závěrem proveďte *Dissolve* dle atributu *TYP_VYUZITI*.

!!! note "&nbsp;<span style="color:#448aff">Nápověda</span>"
      Data se vhodně protřídí dle kódů níže pomocí funkce *Select by attributes* (využití spojky AND pro určení kódů z obou sloupců *SC_D_POZEMKU* a *SC_ZP_VYUZITI_POZ* najednou). Takto vybraným plochám se následně přiřadí nový atribut. 
      
      Například pro určení orné půdy vybereme *SC_D_POZEMKU* = 2. Pro určení zastavěné plochy už budeme muset využít oba sloupce s kódy pozemků, a tedy musíme vybrat *SC_D_POZEMKU* = 13 a *SC_ZP_VYUZITI_POZ*  *is Null*

      V případě určování typu využití pozemku (sloupec *TYP_VYUZITI*) pro atributy *ostatní* a *komunikace* musí platit výběr prvků ze sloupců *Kód druhu pozemku* a *Způsob využití pozemku* zároveň (tedy využití *AND* ve funkci *Select by attributes*).


|  Typ využití pozemku *TYP_VYUZITI* (vypočtené)       | Kód druhu pozemku *SC_D_POZEMKU*        | Způsob využití pozemku *SC_ZP_VYUZITI_POZ*            
| ------------ | ------------------------- |----------------|
| orná půda    | 2 | -|
| lesní půda | 10 |  -|
| trvalý travní porost   | 7, 8 | -|
| zahrada    | 5, 6 | -|
| vodstvo   | 11 | -|
| zastavěná plocha     |  13  | *Null* |
| nádvoří     |  13  | *Not Null* |
| komunikace   | 3, 4 , 14 | 14, 15, 16, 17|
| ostatní   | 3, 4 , 14 | vše kromě 14, 15, 16, 17|

### 5. Georeferencování SMO5

- Georeferencujte rastry Státní mapy 1 : 5 000 – odvozené (SMO5) z 50. let 20. století. Najdete je na disku ```S:\K155\Public\data\GIS\SMO5```. Překopírujte si je na disk počítače.

- Georeferencujte pouze rastry, na kterých se nachází katastrální území, ve kterém leží zadaný bod. Potřebné rastry vyhledáte podle názvu mapových listů, které naleznete ve vrstvě Klad_SMO5: ```S:\K155\Public\155GIS1\Klad_SMO5```.

- Z georeferencovaných rastrů vytvořte mozaiku. Rastrovou mapu SMO5 neexportujte do výsledné webové aplikace.

### 6. Vektorizace využití ploch SMO5
- Na podkladu SMO5 vektorizujte celé katastrální území, ve kterém leží zadaný bod. Tato data následně slučte na základě typů využití ploch (funkce *Dissolve*). 

- Rozlišujte následující typy využití ploch (stejně jako v bodě 5 pro data z RÚIAN): 

    - orná půda

    - lesní půda

    - trvalý travní porosty (louky, pastviny)

    - zahrada

    - vodstvo (řeky, potoky, rybníky), nevektorizujte malé vodní toky vyznačené pouze liniově

    - zastavěná plocha

    - nádvoří (okolí domů, neoznačené zahrady, veřejné prostory v intravilánu)

    - komunikace (cesty, silnice, železnice)

    - ostatní lomy, neúrodná půda apod.

<figure markdown>
![SMO5_legenda](../assets/cviceni6/SMO5_legenda.png "Legenda SMO5"){ width="600" }
    <figcaption>Značkový klíč SMO5</figcaption>
</figure>

### 7. Kontrola topologie vektorizace
- Proveďte topologickou kontrolu vektorizovaných dat SMO5 podle pravidel:

    - Must Not Have Gaps (Area) – nesmí být mezery mezi plochami.

    - Must Not Overlap With (Area-Area) – plochy se nesmí překrývat.

    - Must Not Overlap (Area) – jednotlivé třídy využití se nesmí překrývat.

### 8. Porovnání vývoje využití krajiny (50. léta a současnost)

- Ve webové aplikaci porovnejte vývoj využití krajiny v 50. letech 20. století (vektorizace z SMO5) se současností (RÚIAN – vrstva *Parcela*). Způsob porovnání zvolte dle vlastního uvážení (posuvník v aplikaci, nová vrstva s vypočtenými rozdíly apod.).

### 9. Přidání online mapové služby (WMS, WMTS, WFS)

- Přidejte jednu online mapovou službu dle vlastního výběru (např. historická mapa, ortofoto, katastrální mapa).

- Tato vrstva musí být součástí výsledné mapové aplikace.

### 10. Analýza nejvyššího a nejnižšího bodu obce

- Pomocí digitálního modelu reliéfu (DMR4G nebo DMR5G) zjistěte nejnižší a nejvyšší bod obce. Pro analýzu si vyberte buď DMR4G nebo DMR5G - výběr při prezentaci práce odůvodněte.


### 11. Tvorba webové mapové aplikace

- Vytvořte webovou mapovou aplikaci a vyexportujte do ní požadované vrstvy.

- Přidejte obecné informace o obci, např. popis lokality či vývoj počtu obyvatel.
