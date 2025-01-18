N = 33
K = 12

alien_dict = ['bf', 'biifablhhfekcjfhdklefkiihffedfjkklldcbfdldddbf', 'bikjidjifidghfklddjchiebjbibdjadlgji', 'bkblijbgjbkillhcblbjacadceahebbcafichcjedhbajlfkei',
 'bldgbfhkfdbcihbdkfejkdgikeclih', 'cbielkdheejdicfjfeclbdliidkdcfifdgehlleikkdb', 'cccfckhbglgfi',
  'cjjgibfkgegchldfaclliejhhcbjickadahbcdkialldfb', 'eclbbfcjdfecfdkiblddaceclddfkaabjgalgiggacjdegf', 'efdjhebdfebhhccahifhaififjbadhc',
   'eghcflfgkllde', 'eidbdkcjicecjaiddfdcjkfj', 'ejifhhdiclkkejdhidkhbhjdihbdkckfkgiidhadjdje', 'elacahafeeghdgkic',
    'fag', 'fbeidhlbfhcbjebaegidflileilejkijdfjdkiclabdfjeejeg', 'gebfadchbgcikgkfifaga', 'gialjghjjhhedflkkdjlhajdkhdakhadkkajgllgllbghk',
     'helekchjgeb', 'iehdjcjefggkcafllgedfhjhhiahgc', 'ike', 'ikgjliklfblbagfafe', 'ilfeajblklchcebejiggjhfbdcla',
      'jdlfbhdfjbdblgcceihcgiaachlhlhjhcglhcaf', 'jeahcekiahlkidflijakdj', 'jfhgbkchhgckahefbjcgaceibkiehallgiffddchacigefa',
       'jhlfhckghgkgfb', 'kfcahfciklbakdgehkgfadggdcjcfaijkjlffjf', 'kiidkhfcclldfceahaabjfgdi', 'kjbchgcbbdghhk',
        'lfkdjkkeebibdidhjfkldkhecllebheehjhcaileeggafii', 'lhd' 'lkkkldcfbfekbjdfalhiddaiegkf', 'lljjjgj']
        
print(len(alien_dict))
adj = [[] for i in range(K)]
map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
for i in range(N - 1):
    for j in range(min(len(alien_dict[i]), len(alien_dict[i + 1]))):
        if alien_dict[i][j] != alien_dict[i + 1][j]:
            adj[map[alien_dict[i][j]] - 1].append(map[alien_dict[i + 1][j]] - 1)
            break
vis = {}
ans = []
def dfs(i):
    vis[i] = 1
    for j in adj[i]:
        if j not in vis:
            dfs(j)
    ans.append(i)
for i in range(len(adj)):
    if i not in vis:
        dfs(i)
ans.reverse()    
key_list = list(map.keys())
values_list = list(map.values())
for i in range(len(ans)):
    ans[i] = key_list[values_list.index(ans[i] + 1)]
print(ans)