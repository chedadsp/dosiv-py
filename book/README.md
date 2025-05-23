# Обрада слике и видеа код системима заснованих на рачунару

## Садржај

## Предговор

## Како се чита ова књига

## Мотивација као увод

## Дигитализација слике

### Семпловање и својства сигнала

### Рачунарски вид

### Простори боја

## Камере

### Карактеристике камера

### Параметри камере

### Разнилите примене камере

### Модерни дизајн

### Остали сензори

## Припрема слике за даљу обраду

### Филтрирање

### Харова обележја

### Интегрална слика (како се рачуна, чему слижи)

### Хистограм

### Корекција боја

### Филтрирање по боји (начин рада, предности, недостаци)

## Детекција ивица

### Како се ради детекција ивице?

### Метод градијента - изглед кернела и примена

### Robert Cross оператор (кернел и примена прага)

### Остали оператори (навести који постоје)

### Canny оператер (начин рада)

## Сегментација слике

### Захтеви и услови сегментације

### Врсте сегментације

### амплитуда сегментација (ручна/адаптивна - када који? Зашто? Недостаци?)

### сегментација на основу ивице (локална обрада, интерполација криве)

### сегментација на основу раста површине  (врсте и примери)

### сегментација груписањем (K-means clustering)

### Препознавање линија

#### Хаф

#### Рансак

#### ??? полиноми

#### Шта још има?

## Детекција објеката

### Детекција или идентификација

### Изазови код детекције

### Мера квалитета

### Детекција помоћу шаблона

### Можемо ли боље (обележја)?

### Одлике добрих обележја

### Издвајање обележја

### DoG - начин рада (објаснити скицу)

### HOG – начин рада и примена

### SIFT - начин рада (кораци, недостаци)

### Остале методе (навести које постоје и дати основне информације)

### детекције објеката помоћу обележја

## Реконструкција треће димензије

### Математички модел облика тела

### Положај тела у односу на друго тело

### Трансформација координата између координатних система

### Математички модел камере

### Параметри камере

### Облак тачака

### Стерео визија

### Епиполарна геометрија

### Проблем кореспонденције

### Фундаментална матрица

### Калибрација камера

## Анализа покрета

### Кретање у слици

### Одузимање позадине (BS)

### детекција предњег плана (FD)

### Дијаграм тока BS алгоритма

### Моделирање позадине (технике и примери)

### Детекција предњег плана

### Значај пред и пост обраде

### Алгоритми за праћење покретних објеката

#### Mean-Shift

#### Camshift

#### Optical flow

### Хафманов филтер

## Алгоритми машинског учења

### Генерални принципи

### Врсте машинског учења

### Надзирани

### Ненадзирани

### Хибридни

### Viola-Jones алгоритам

### Ada-Boost алгоритам (принцип рада, јаки/слаби класификатори)

### Каскада класификатора

### Предности и недостаци Виола-Јонес алгоритма

## Дубоке неуронске мреже

### Основни појмови

### Топологије мреже

### YoLo

### Модерни приступи у потрошачкој електроници

### Модерни приступи у аутобилској индустрији

## Примена рачураске визије

### Како дизајнирати свој алгоритам?

#### Описати анализу проблема?

#### Урадити одабир камере?

#### Дизајн алгоритма

#### Процена потребних ресурса

#### Како потврдити решење?

#### Буилд фор тест

#### Испитивање у реалним условима

### Потрошачка електроника

#### Поправка ужитка (припрема за инстаграм)

#### Ноћни режим

#### Убрзани снимак

#### Слоу моушн

#### Оверлеји и филтери

#### Детекција лица

#### Стабилизација слике

#### Проширена стварност

### Аутомобилска индустрија

#### Поглед одозго на возило и подручје око њега

#### Детекција паркинг места и помоћ при паркирању

#### Детекција траке и упозорење о напуштању траке

#### Детекција објеката (пешака, саобраћајних знакова, возила)

#### Праћење возача

#### Замена огледала камере

## Смернице за даље учење
