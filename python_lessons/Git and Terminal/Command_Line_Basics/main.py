# Command line nevigation

# pwd - використовується для визначеня в який ти деректорії

# Ви можете переглянути вміст поточного каталогу за допомогою команди ls (скорочено від list - список).

# Якщо нам потрібна більш детальна інформація, ми можемо додати ключ -l і відобразити вміст у вигляді списку.

# За замовчуванням ми бачимо лише звичайні файли і теки і не бачимо приховані, назви яких починаються з ... Ключ -a покаже і їх.

# Сортування файлів і тек за датою (а не за назвою) можна виконати за допомогою ключа -t. Її також можна комбінувати з іншими.

# ./ на початку шляху означає, що ми починаємо з поточного каталогу, відкриваємо папку Movies, в якій має бути папка Avengers, вміст якої буде надруковано.

# Цей самий шлях можна вказати і без ./. За замовчуванням, термінал шукатиме файл або теку у поточному каталозі

# Але іноді замість відносного шляху зручніше використовувати абсолютний шлях, який починається з кореня /
# Щоб скопіювати каталог, потрібно додати ключ -r (рекурсивно), щоб він був скопійований разом з усім вмістом.
# Ви також можете почати шлях з ~, що означає домашній каталог поточного користувача

# Щоб перейти до іншого каталогу, використовуйте команду cd (скорочення від change directory - змінити каталог). Після неї вкажіть шлях до каталогу у тому ж форматі, що і для команди ls.

# -------------------------------------------------->

# Manipulating files and folders


# Команда cat > file.name дозволяє створити файл і ввести його вміст рядок за рядком.
#
# За допомогою команди cat file.name можна вивести вміст файлу на екран.
#
# Команда touch дозволяє створити порожній файл,

# Команда mkdir відповідає за створення каталогів. Ключ -p дозволяє створювати декілька вкладених каталогів.

# Команда mv дозволяє перейменовувати файли і каталоги. Для цього потрібно вказати шлях до існуючого файлу або каталогу, а потім шлях з новим неіснуючим ім'ям.

# Щоб скопіювати каталог, потрібно додати ключ -r (рекурсивно), щоб він був скопійований разом з усім вмістом.

# За замовчуванням команда rm видаляє лише звичайні файли. Для системних файлів вона запитує підтвердження. Для видалення без необхідності підтвердження вручну, ви можете додати прапорець -f.
# Ви також можете вказати декілька файлів через пробіл, щоб видалити їх разом.
# Для видалення каталогів слід додати ключ -r (рекурсивно). Його можна комбінувати з ключем -f:
# відкрийте картинку під назвою Manipulating files and folders

# * у шляху означає будь-яку назву, тому rm -r src/* видалить увесь вміст каталогу src.

# -------------------------------------------------->

# Reading file content


# відкрийте картинку з назвою Files and Folders


# • Скористайтеся цією командою, щоб знайти потрібний вам файл.
# Вона працює, як команда пошуку в Windows. Крім того, аргумент -i
# робить команду нечутливою до регістру, завдяки чому ви зможете
# шукати файли, навіть якщо ви не пам'ятаєте їх точні назви.
# • Щоб знайти файл, що містить два або більше слова, використовуйте
# зв’язку (*) . Наприклад, команда locate -i school*note буде шукати
# будь-який файл, що містить слова «school» і «note», не залежачи від
# того, що вони написані великою або маленькою буквою.

# -------------------------------------------------->

# Reading files with Less
# відкрийте картинку з назвою Files and Folders

# -------------------------------------------------->

# Command Line Documentation

# щоб дізнатися більше про команду треба написати --help і відкриється в консолі документація
# приклад: grep --help, pwd --help mv --help і так далі

# -------------------------------------------------->

# Commans History
# відкрий зошит або картинку з назвою Command History


# -------------------------------------------------->

# Pipes and Redirects

# відкрийте картинку з назвою Basic Commands


# -------------------------------------------------->

# Creating own dhell scripts
# відкрийте картинку з назвою creating_shell_scripts

# -------------------------------------------------->

# Aliases