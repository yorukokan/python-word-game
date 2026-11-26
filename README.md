<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1E1B4B,50:7C3AED,100:10B981&height=210&section=header&text=Python%20Word%20Game&fontSize=42&fontColor=F8FAFC&fontAlignY=38&desc=CLI%20Word%20Guessing%20Game%20%E2%80%A2%20Dynamic%20Hints%20%C2%B7%20Adaptive%20Attempts%20%C2%B7%20Scoring%20Engine&descSize=16&descAlignY=62&animation=fadeIn" alt="Python Word Game Banner" />

<a href="https://github.com/yorukokan/python-word-game">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2600&pause=900&color=A78BFA&center=true&vCenter=true&width=780&lines=Interactive+Python+3+CLI+Word+Guessing+Game;100+CS+%26+Tech+Vocabulary+Entries+%C2%B7+Zero+External+Dependencies;Dinamik+%C4%B0pucu%2C+Karek%C3%B6k+Tabanl%C4%B1+Hak+ve+Puanlama+Sistemi;Sesli%2FSessiz+Harf+Puanlamas%C4%B1+%C2%B7+Hatas%C4%B1z+Tahmin+Bonusu" alt="Typing SVG" />
</a>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0B0F19" alt="Python 3" />
  <a href="https://github.com/yorukokan">
    <img src="https://img.shields.io/badge/GitHub-yorukokan-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0B0F19" alt="GitHub" />
  </a>
  <a href="https://linkedin.com/in/okanyoruk">
    <img src="https://img.shields.io/badge/LinkedIn-okanyoruk-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0B0F19" alt="LinkedIn" />
  </a>
  <a href="mailto:okanyoruk.tr@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0B0F19" alt="Email" />
  </a>
</p>

</div>

---

## 🎯 Overview · Proje Özeti

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🇬🇧 English</h3>
      <p>
        <b>Python Word Game</b> is a lightweight, zero-dependency terminal word guessing game written in pure Python 3 (<code>Python-Word-Game.py</code>). It challenges players to uncover computer science and technology terms drawn randomly from a built-in 100-entry word bank (97 unique words) without repeating words within the same session.
      </p>
      <p>
        Each round dynamically scales its difficulty based on word length: revealing <code>len(word) // 3</code> unique hint letters, calculating allowed mistakes via <code>ceil(sqrt(len(word)))</code>, and scoring guesses according to vowel/consonant frequency, penalties, and a flawless-round bonus.
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🇹🇷 Türkçe</h3>
      <p>
        <b>Python Word Game</b>, harici bağımlılık gerektirmeden saf Python 3 ile geliştirilmiş (<code>Python-Word-Game.py</code>) etkileşimli bir komut satırı kelime tahmin oyunudur. Oyuncular, yerleşik 100 girdilik (97 benzersiz) bilgisayar bilimleri ve teknoloji kelimesi havuzundan rastgele seçilen kelimeleri aynı oturumda tekrar etmeden tahmin etmeye çalışır.
      </p>
      <p>
        Her tur kelime uzunluğuna göre dinamik olarak ölçeklenir: <code>len(kelime) // 3</code> adet benzersiz ipucu harfi açılır, tahmin hakkı <code>ceil(sqrt(len(kelime)))</code> formülüyle belirlenir ve puanlama sesli/sessiz harf tekrarına, yanlış tahmin cezasına ve hatasız bitirme bonusuna göre hesaplanır.
      </p>
    </td>
  </tr>
</table>

---

## ✨ Key Features · Öne Çıkan Özellikler

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🎲 Non-Repeating CS Word Bank</h4>
      <b>EN:</b> Randomly selects from 100 English computer science entries (97 unique words) and tracks played words in <code>onceki_kelimeler</code> to avoid duplicates in a session.<br/>
      <b>TR:</b> 100 girdilik (97 benzersiz) İngilizce bilgisayar bilimleri kelime listesinden rastgele seçim yapar ve aynı oturumda tekrarı önlemek için <code>onceki_kelimeler</code> listesini kullanır.<br/><br/>
      <code>Python-Word-Game.py</code> · <code>Kelime_listesi</code>
    </td>
    <td width="50%" valign="top">
      <h4>💡 Dynamic Hint Generation</h4>
      <b>EN:</b> Automatically reveals <code>len(kelime) // 3</code> distinct random letters before guessing starts and displays masked progress with underscores (<code>_</code>).<br/>
      <b>TR:</b> Tahmin başlamadan önce <code>len(kelime) // 3</code> adet benzersiz harfi rastgele ipucu olarak açar ve kelime durumunu alt çizgilerle (<code>_</code>) gösterir.<br/><br/>
      <code>Python-Word-Game.py</code> · <code>ipucu_harf</code>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>📐 Adaptive Attempt Calculation</h4>
      <b>EN:</b> Computes attempts using the ceiling square root of word length: exact squares keep <code>int(sqrt(n))</code>, while non-squares add <code>+1</code>.<br/>
      <b>TR:</b> Tahmin hakkını kelime uzunluğunun yukarı yuvarlanmış kareköküyle hesaplar: tam kare uzunluklar <code>int(sqrt(n))</code> olarak kalır, diğerlerine <code>+1</code> eklenir.<br/><br/>
      <code>Python-Word-Game.py</code> · <code>tahmin_hak</code>
    </td>
    <td width="50%" valign="top">
      <h4>🏆 Frequency &amp; Bonus Scoring</h4>
      <b>EN:</b> Awards <code>+4 × count</code> for vowels (<code>aeıioöuü</code>), <code>+3 × count</code> for consonants, <code>-5</code> for wrong guesses, and a <code>+5</code> bonus for zero-mistake wins.<br/>
      <b>TR:</b> Sesli harfler (<code>aeıioöuü</code>) için <code>+4 × adet</code>, sessiz harfler için <code>+3 × adet</code>, yanlış tahminlerde <code>-5</code> puan ve hatasız bitirmede <code>+5</code> bonus verir.<br/><br/>
      <code>Python-Word-Game.py</code> · <code>puan</code>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🛡️ Input Normalization &amp; Guards</h4>
      <b>EN:</b> Normalizes input with <code>.lower()</code> and blocks re-guessing hint letters or previously entered letters without deducting attempts.<br/>
      <b>TR:</b> Girilen harfi <code>.lower()</code> ile küçültür; ipucu olarak verilen veya daha önce tahmin edilen harfleri hak düşürmeden engeller.<br/><br/>
      <code>Python-Word-Game.py</code> · <code>dogru_harf</code> · <code>yanlis_harf</code>
    </td>
    <td width="50%" valign="top">
      <h4>🔁 Continuous Replay Menu</h4>
      <b>EN:</b> Prompts at the end of every win or loss to start a new word (<code>1</code>) or exit cleanly (<code>2</code>) while preserving session word history.<br/>
      <b>TR:</b> Her kazanma veya kaybetme sonrası oturumdaki kelime geçmişini koruyarak yeni kelimeye geçme (<code>1</code>) veya çıkış yapma (<code>2</code>) seçeneği sunar.<br/><br/>
      <code>Python-Word-Game.py</code> · <code>secim</code>
    </td>
  </tr>
</table>

### 🧮 Scoring & Mechanics Summary · Puanlama ve Mekanik Özeti

| Rule · Kural | Formula / Condition · Formül / Koşul | Effect · Etki |
| :--- | :--- | :--- |
| **Hints · İpucu Sayısı** | `len(kelime) // 3` | Distinct letters revealed at round start |
| **Attempts · Tahmin Hakkı** | `int(sqrt(n))` if perfect square, else `int(sqrt(n)) + 1` | Allowed wrong guesses per round |
| **Correct Vowel · Doğru Sesli Harf** | `tahmin_harf in "aeıioöuü"` | `+4 * sayac` points (`sayac` = occurrences) |
| **Correct Consonant · Doğru Sessiz Harf** | `tahmin_harf not in "aeıioöuü"` | `+3 * sayac` points (`sayac` = occurrences) |
| **Wrong Guess · Yanlış Tahmin** | `tahmin_harf not in kelime` | `-5` points and `tahmin_hak -= 1` |
| **Flawless Win · Hatasız Bitiş Bonusu** | All letters revealed and `tahmin_hak == kontrol_hak` | `+5` bonus points |

---

## 🏗️ Architecture · Mimari

```text
Python-Word-Game.py (Single-File CLI Loop)
│
├── 1. Session Setup
│     ├── Kelime_listesi (100 CS terms, 97 unique)
│     └── onceki_kelimeler[] (session history)
│
├── 2. Outer Game Loop (while True)
│     ├── random.randint() ──▶ pick unseen `kelime`
│     ├── ipucu = len(kelime) // 3 ──▶ populate `ipucu_harf`
│     └── tahmin_hak = ceil(sqrt(len(kelime))) ──▶ store `kontrol_hak`
│
├── 3. Inner Round Loop (while tahmin_hak > 0)
│     ├── Render status (attempts, score, guessed letters, masked word)
│     ├── Read & lowercase `tahmin_harf`
│     │     ├── In `ipucu_harf`? ──▶ warn & re-prompt
│     │     └── In `dogru_harf` / `yanlis_harf`? ──▶ warn & continue
│     ├── Match in `kelime`?
│     │     ├── YES ──▶ count `sayac` ──▶ +4*sayac (vowel) or +3*sayac (consonant)
│     │     │          └── All letters revealed? ──▶ +5 bonus if flawless ──▶ WIN
│     │     └── NO  ──▶ -5 points, tahmin_hak -= 1
│     │                └── tahmin_hak == 0? ──▶ reveal word ──▶ LOSS
│
└── 4. Post-Round Menu
      ├── Append `kelime` to `onceki_kelimeler`
      └── Input `secim`: `1` (New Word) │ `2` or other (Exit)
```

---

## 🛠️ Tech Stack · Teknoloji Yığını

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117)
![Standard Library](https://img.shields.io/badge/Stdlib-random-10B981?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117)
![CLI](https://img.shields.io/badge/Interface-CLI%20Terminal-7C3AED?style=for-the-badge&logo=gnubash&logoColor=white&labelColor=0D1117)

</div>

---

## 📂 Project Structure · Proje Yapısı

```text
python-word-game/
├── Python-Word-Game.py   # Main single-file word guessing game (173 lines)
├── .gitattributes        # LF line-ending normalization rules
├── .gitignore            # Standard Python ignore rules
└── README.md             # Project documentation
```

---

## 🚀 Getting Started · Kurulum ve Çalıştırma

### Prerequisites · Gereksinimler
- **Python 3.x** installed on your system (no external packages required).

### Installation & Run · Kurulum ve Çalıştırma

```bash
# 1. Clone the repository · Depoyu klonlayın
git clone https://github.com/yorukokan/python-word-game.git
cd python-word-game

# 2. Run the game · Oyunu başlatın (Linux / macOS)
python3 Python-Word-Game.py

# Windows
python Python-Word-Game.py
```

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1E1B4B,50:7C3AED,100:10B981&height=100&section=footer" alt="Footer Banner" />

<sub>⚡ <b>Okan Yörük</b> · Python Word Game · <a href="https://github.com/yorukokan">github.com/yorukokan</a></sub>

</div>
