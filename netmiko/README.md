# Python script

### Mi a program feladata?
A program célja a ’user’ nevű felhasználó SSH jelszavának cseréje az összes IP cím alapján meghatározott eszközön.

### Milyen célokat valósít meg?
Egyszerre több eszközön működik és jelentősen meggyorsítja az eszközök jelszavának cseréjét.

### Milyen bemenő adatokkal dolgozik?
- A program bekér egy kulcsot az AES titkosításhoz.
- Beolvassa az ’ips.txt’ fájlt a cél eszközök meghatározására.
- Beolvassa a ’hash.txt’ fájlt ami a kulcs sha256 hash-ét tárolja annak ellenőrzésére.
- Beolvassa a ’pass.txt’ fájlt amiból kiolvassa a BASE64 szövegként tárolt AES titkosítás initialization vector-át és AES-el titkosított SSH jelszavat.

### Milyen kimenetet produkál helyes működés és hiba esetén?
Helyes működés esetén a program jelzi, hogy sikeresen módosította az SSH jelszót, hiba esetén pedig, hogy hibába ütközött. A fájlban tárolt jelszót minden esetben cseréli.

### Milyen lépéseket hajt végre a program?
1. Bekér egy kulcsot a titkosításhoz
2. Ellenőrzi a kulcsot
3. Kiolvassa a titkosított SSH jelszavat
4. Véletlenszerűen generál egy új jeszavat és eltárolja titkosítva
5. Bejelentkezik az érintett eszközökre és módosítja a jelszavat az újra

### Milyen hibakezelést használ?
A program egy try-except blokkot használ az SSH kapcsolatok használatakor.

> Az alap `pass` kulcs hash-e a `d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1`

# Fájlok

### hash.txt
Az AES titkosításhoz használt kulcs hash-ét tárolja és csak ellenőrzére van használva.

### ips.txt
Soronként egy IP címet tartalmaz, ezekre a címekre próbál a program kapcsolódni SSH-n keresztül.

### enable.txt és pass.txt
A fájl első sora az AES titkosítás feloldásához szükséges base64 kódolású initialization vector-t tárolja.\
A második sor magát a titkosított jelszót tárolja base64-el kódolva.
