N = 33
K = 12

dict = ['bf', 'biifablhhfekcjfhdklefkiihffedfjkklldcbfdldddbf', 'bikjidjifidghfklddjchiebjbibdjadlgji', 'bkblijbgjbkillhcblbjacadceahebbcafichcjedhbajlfkei',
 'bldgbfhkfdbcihbdkfejkdgikeclih', 'cbielkdheejdicfjfeclbdliidkdcfifdgehlleikkdb', 'cccfckhbglgfi',
  'cjjgibfkgegchldfaclliejhhcbjickadahbcdkialldfb', 'eclbbfcjdfecfdkiblddaceclddfkaabjgalgiggacjdegf', 'efdjhebdfebhhccahifhaififjbadhc',
   'eghcflfgkllde', 'eidbdkcjicecjaiddfdcjkfj', 'ejifhhdiclkkejdhidkhbhjdihbdkckfkgiidhadjdje', 'elacahafeeghdgkic',
    'fag', 'fbeidhlbfhcbjebaegidflileilejkijdfjdkiclabdfjeejeg', 'gebfadchbgcikgkfifaga', 'gialjghjjhhedflkkdjlhajdkhdakhadkkajgllgllbghk',
     'helekchjgeb', 'iehdjcjefggkcafllgedfhjhhiahgc', 'ike', 'ikgjliklfblbagfafe', 'ilfeajblklchcebejiggjhfbdcla',
      'jdlfbhdfjbdblgcceihcgiaachlhlhjhcglhcaf', 'jeahcekiahlkidflijakdj', 'jfhgbkchhgckahefbjcgaceibkiehallgiffddchacigefa',
       'jhlfhckghgkgfb', 'kfcahfciklbakdgehkgfadggdcjcfaijkjlffjf', 'kiidkhfcclldfceahaabjfgdi', 'kjbchgcbbdghhk',
        'lfkdjkkeebibdidhjfkldkhecllebheehjhcaileeggafii', 'lhd' 'lkkkldcfbfekbjdfalhiddaiegkf', 'lljjjgj']

adj = [[] for i in range(K)]

for i in range(N - 1):
    s1 = dict[i]
    s2 = dict[i + 1]
    for j in range(min(len(s1), len(s2))):
        if s1[j] != s2[j]:
            adj[ord(s1[j]) - ord('a')].append(ord(s2[j])- ord('a'))
            break
vis = {}
ans = []
def dfs(i):
    vis[i] = 1
    for j in adj[i]:
        if j not in vis:
            dfs(j)
    ans.append(chr(i + ord('a')))
for i in range(len(adj)):
    if i not in vis:
        dfs(i)
ans.reverse()    
print(ans)