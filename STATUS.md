change MOVELOG_PANEL_HEIGHT to accomodate back button; move log button keeps drawing over the back button(-80)

rearrange directories for easy navigation

change indentation of ChessMain and ChessAI

add GameFunctions, Constants, Button, Design, Page

add menu and basic ui

add board, piece, background buttons
    add piece selection
    add board option buttons

change all variables to either camelcase(except for in_check in ChessEngine because there is a function called inCheck())

todo: add sounds to clicks; mouse hover; piece(checked off - ABBY), board and bg customization

as of 8.11.23 TODO:
- make background page and customization
- ABBY DESIGN -> robot expressions, 1 more piece set?, settings module boxes
- ardit -> add multilevel bots
- general -> add bot selection screen, add meet the creators screen??

abby completed 8.14.23:
- added organic and royal piece sets
- added 3 new boards and completed boards page
- updated piece previews -> not final might round the corners more/make semi-transparent
- logo on homescreen + new background


abby completed 8.15.23:
- AI opponent selection page -> header, AI names, icon, box for text, individual play buttons (all take to same game rn)
- deleted the drawSettings function that was commented out and not being used
- shifted homescreen buttons down slightly
- set default background to agreed upon purple + black combo


abby 8.17.23:
- adjusted piece buttons, board buttons -> reverted board settings back button to standard
- play buttons for AI select now black per request
- recolored black organic piece set
- added team defeat icons
- replaced key page with creator page and added basic info (will add roles, linkedin info soon)
- redid the god-awful looking piece example images
- provided 1 text bubble -> subject for modification


also:



  __QQ                       ;,'   QQ__
 (_)_">         _o_       ;:;'    <"_(_)
_/          ,-.'---`.__ ;              _\
           ||j`=====',-'
            `-\     /
               `-=-' 

___  ___                       _____           ______          _         _ 
|  \/  |                      |_   _|          | ___ \        | |       | |
| .  . | ___  _   _ ___  ___    | | ___  __ _  | |_/ /_ _ _ __| |_ _   _| |
| |\/| |/ _ \| | | / __|/ _ \   | |/ _ \/ _` | |  __/ _` | '__| __| | | | |
| |  | | (_) | |_| \__ \  __/   | |  __/ ()_| | | | | ()_| | |  | |_| |_| |
\_|  |_/\___/ \__,_|___/\___|   \_/\___|\__,_| \_|  \__,_|_|   \__|\__, (_)
                                                                    __/ |  
                                                                   |___/ 


