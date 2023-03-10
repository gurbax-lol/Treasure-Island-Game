print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

door_message = '''
  *******************************************************************************
      ______                ______                ______
   ,-' ;  ! `-.          ,-' ;  ! `-.          ,-' ;  ! `-.
  / :  !  :  . \        / :  !  :  . \        / :  !  :  . \
 |_ ;   __:  ;  |      |_ ;   __:  ;  |      |_ ;   __:  ;  |      
 )| .  :)(.  !  |      )| .  :)(.  !  |      )| .  :)(.  !  |
 |"    (RED) _  |      |"  (YELLOW) _ |      |"   (BLUE) _  |
 |  :  ;`'  (_) (      |  :  ;`'  (_) (      |  :  ;`'  (_) (
 |  :  :  .     |      |  :  :  .     |      |  :  :  .     |
 )_ !  ,  ;  ;  |      )_ !  ,  ;  ;  |      )_ !  ,  ;  ;  |
 || .  .  :  :  |      || .  .  :  :  |      || .  .  :  :  |
 |" .  |  :  .  |      |" .  |  :  .  |      |" .  |  :  .  |
 |_____;----.___|      |_____;----.___|      |_____;----.___|
  *******************************************************************************
      GOOD GOD! NOW THERE ARE 3 DOORS IN FRONT OF YOU
'''
winning_message = '''
        ,,,,,,,,,,,,,
    .;;;;;;;;;;;;;;;;;;;,.
  .;;;;;;;;;;;;;;;;;;;;;;;;,
.;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
;;;;;@;;;;;;;;;;;;;;;;;;;;;;;;' .............
;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'.................
;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'...................
`;;;;@;;;;;;;;;;;;;;;@;;;;;;;'.....................
 `;;;;;;;;;;;;;;;;;;;@@;;;;;'..................;....
   `;;;;;;;;;;;;;;;;@@;;;;'....................;;...
     `;;;;;;;;;;;;;@;;;;'...;.................;;....
        `;;;;;;;;;;;;'   ...;;...............;.....
           `;;;;;;'        ...;;..................
              ;;              ..;...............
              `                  ............
             `                      ......
            `                         ..
           `                           '
          `                           '
         `                           '
        `                           `
        `                           `,
        `
         `
           `.
           YOU WIN!
'''

fire_message = '''
  *******************************************************************************
                            (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
         )            . `--=.._____..=--'. ./  

                    YOU HAVE DIED IN A FIRE! 
                           GAME OVER.
   *******************************************************************************
'''

bear_message = '''
*******************************************************************************
   _,-""`""-~`)
(`~           \
 |     a   a   \
 ;        o     ; ___  _,,,,_     _.-~'.
  \      `^`    /`_.-"~      `~-;`      \
   \_      _  .'                 `,     |
     |`-                           \'__/
    /                      ,_       \  `'-.
   /    .-""~~--.            `"-,   ;_    /
  |              \               \  | `""`
   \__.--'`"-.   /_               |'
              `"`  `~~~---..,     |
                            \ _.-'`-.
                              \       \
                               '.     /
                                 `"~"`
                    OH NO! YOU WERE EATEN BY A BEAR!
                               GAME OVER.
*******************************************************************************

'''

guard_message = '''
  *******************************************************************************
  ,^.
  |||
  |||       _T_
  |||   .-.[:|:].-.
  ===_ /\|  "'"  |/
   E]_|\/ \--|-|''  |
   O  `'  '=[:]| A  |
          /""""|  P |
         /"""""`.__.'
        []"/"""\"[]
        | \     / |
        | |     | |
      <\\\)     (///>
  *******************************************************************************
        YOU WERE ATTACKED BY A GUARD AND DIED!
'''

fall_message = '''
*******************************************************************************
  _      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_     _     _     _     _     _     _     _
)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,
_    _    _    _    _    _    _    _    _
)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,
 _       _      _       _      _      _
( `'-.,_( `'-.,( `'-.,_( `'-._( `'-.,( `'-.,
 _    _     _      _
( '-.( '-.,( '-.,_( `'-.,_
   _     _     _     _     _     _
__( '-._( '-._( '-._( '-._( '-._( '-.__
  (_.-' (_.-' (_.-' (_.-' (_.-' (_.-'
   _     _     _     _     _     _
__) '-._) '-._) '-._) '-._) '-._0) '-.__
  )_.-' )_.-' )_.-' )_.-' )_.-' 0)_.-'

``'-.,_,.-'``'-.,_,.='``'-.,_,.-'``'-.,_,.='``

.-.   .-.   .-.   .-.   .-.   .-.   .-.   .-.   .-.
   '-'   '-'   '-'   '-'   '-'   '-'   '-'   '-'   '-'
*******************************************************************************
            YOU FELL INTO A LAVA! GAME OVER.
'''

water_message = '''
*******************************************************************************

   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `

   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `

   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `

   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `
*******************************************************************************
            WATCH OUT FOR THE HUGE WAVES!

'''
direction = input("Left or right?\n").lower()

if direction == "left":
  print(water_message)
  action = input("Swim or wait?\n").lower()
  if action == "wait":
    print(door_message)
    door = input("Which door?\n").lower()
    if door == "yellow":
      print(winning_message)
    elif door == "red":
      print(fire_message)
    elif door == "blue":
      print(bear_message)
    else:
      print("Game over.")
  else:
    print(guard_message)
else:
  print(bear_message)
