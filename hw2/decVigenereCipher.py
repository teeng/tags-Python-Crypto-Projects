from genFunctions import *

# decrypt the Vigenere Cipher through language analysis

def substring(y, m):
  substrings = []
  for i in range(m):
    substring = y[i::m]
    substrings.append(substring)
  return substrings

def encVig(plaintext_numbers, shifts):
    encrypted_text = []
    key_length = len(shifts)
    for i, num in enumerate(plaintext_numbers):
        shift = shifts[i % key_length]
        encrypted_num = (num + shift) % 26
        encrypted_char = chr(encrypted_num + ord('a'))
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

def getR0(substrings):
  R0 = []
  freqs = []
  for seq in range(len(substrings)):
    check = substrings[seq]
    count, freq = counter(check, 26)

    sum = 0
    for j in range(len(freq)):
      sum = sum + freq[j]**2
    R0.append(sum)
    freqs.append(freq)
  return R0, freqs

def getCk(substrings, m):
  Cks = [[0.0] for _ in range(m)]
  freqs = []
  for seq in range(m):
    curr = substrings[seq] # for the current substring
    count, freq = counter(curr, 26)

    # Calculate cross-correlation for each letter
    for shift in range(26):
      correlation = 0.0
      for letter in range(26):
        p = base_freq[letter]
        qk = freq[(letter - shift) % 26]
        correlation += p * qk
      Cks[seq].append(correlation)
    freqs.append(freq)
  return Cks, freqs

def find_m(y, m_min, m_max):
  min_mse, desired_m = 100, len(y) # init
  desired_substrings = None
  desired_freq = None
  for i in range(m_min, m_max):
    substrings = substring(y, i)
    R0, freqs = getR0(substrings)

    ideal = .0656 # from english language
    sum = 0.0
    for j in range(len(R0)):
      err = (R0[j] - ideal)**2
      sum = sum + err
    mse = sum / len(R0)

    if (mse < min_mse):
      desired_m = i
      desired_substrings = substrings
      desired_freqs = freqs
      min_mse = mse
  print(f'Minimum mse: {min_mse} at m = {desired_m}') # with substrings:\n{desired_substrings}')
  return desired_m, desired_substrings, desired_freqs

def decVigenere(cipher, m_min=1, m_max=12):
  y = textToNum(cipher)
  desired_m, desired_substrings, desired_freqs = find_m(y, m_min, m_max)
  key = []
  Cks, freq = getCk(desired_substrings, desired_m)
  for i in range(desired_m):
    key.append(Cks[i].index(max(Cks[i]))-1)
  print(f'key: {key}')

  x = []
  for i in range(0, len(y), desired_m):
    for j in range(desired_m):
      if (i + j < len(y)):
        x.append(y[i+j] + key[j])
  return x

print("\nProblem 9a")
y = "KTSVFVMHMCHJUBFDYLMGRWZXNHMVDSVNUBJOJULFZNAQILXSXOJYOROEFJTDXWCNERALABFMLVJFFSEFVXLUJQBORDKMLFBVGYNXLSNJQDWARDXQHAMBRHUPGTYXVVUYXEXHAQJVMLJEZFZBVQPBYPQMPBCUJHBUDSKQFOTVTFGKYXNPDWXJQYVOWLJDUJNJHBUUFUPFOFUTCLWKFJWMKDMOLYNZSQBVBJJHWEEQHLLWTWTORYZXXDYZXOVFPMIHXBMEHSSHZRZKXORYWAPSTZNURNUEFVYPWTRZAQBIWPLBQXLLVUNARFVNNJWHFZCBUYVOBVYVWJVMTNOWFJLVVYVVFGFZRXDXAXIRQTNTVHBAJRZZOBFZSCJHXAQJVXBMEHSPWUUZZRPQNUCPPDTXTWNUCJPFANUKTBPIWXDJTXYANSODPWFAUSRDDGSN"

x = decVigenere(y)
print(f'plaintext: {numToText(x)}')

print("\nProblem 9b")
y = "KQRAUHSQGGBFDQSXOIXMRWCSYFWAAPPOSELGYQGWZGLDCXVFZZIHLCAXILVRTEWGSJPFLWWCWUXAJOWNEFKGHTMUOVLHIUVBYQGLLRETIEDWETEFVHSQVSUREAEKZIXQEEVBRFLWWCHQVKVTETIWHFETXZLGPBEJHHPMRVLEFMPKAOEUSFACHTMUOHSQPSDGZRRSAICQEFKCQZELBFPEKGKSYFMLSSETIEHRPOIFAFPETWJHEAXZLCAURAVBDAJEHBVURVYSBGMJLGETELAVPKWZVIWPHWJZLDILOSNMYKLGHTMUOWXBIDAVPYXGAVPEIHHFLFMGU"

x = decVigenere(y, m_min=6, m_max=7) # trying m through kasiski test
print(f'plaintext: {numToText(x)}')

print("\nProblem 9c")
y = "GGAMGHUMEDWXUFFAOQLYYSALSHUMEDDXPDVUMAKREIKLAZFEMJQHKKBYKQKYSHVRQFATXMMSFBAHZBXHXHQCGOLERXXTOPPYFBMFRPNVFPZULZWTFQBIYQTHLRTVCAVSKFTWKZFLJGKNXNUVFALYLFRSIXVUHOVJWHVLGOLOHSXTPQFVMQGHVNRQRKTQLXEVGPRCLZBKXWGZEFWFHLVPREVJRQRNWJPHAVDZBSESFFGPVZMTQPVERTHFBHEACKNSFEBXSUEOLWAAZWEEJFPHSSHWMIJJFJYKIYECCILZPEBSGAWARZATXXXJFVBMZUWJGWCKALSMMYERMPGOHFWTRDVQNYNQMBIPMKRZZQLNRIJBPYFBMTKGCMUPJMELSGKQUTZFAJQHGIILZNNYMCUQRHKQQUPDKQJLHWGJWHGPVUATXNVXOMYLTQGYEIKLALCQGYLDWDUAOQZTEAJXFILQGYLTUXZLATXRIIJLQZHZWYIRJKVXBQLTJRTVCAHZTQCHKPUHCQVMECIBQKYMLYMRCIYFATKTYVJQULOULYSGALSJYKIYSVTXCOFMWFTIKKTAVUGHVTCPVUNOKDTIQDEHWTBHGDOMYLEUMDVPPDVUNRKTQIJBCLUMGITPRBETLFATHHQCGOLBTXXIJOBBNTFFGWKKRZSUDJXWGYEPAULMFDOYRZHZWHSAQPFBZOHRTJVBEZHFUQIIEEYLFBTWOXPTBYSPPFVXKQBAOQFFXWGJNAPOTQPNCAIHUOXIGDOMHALDBEISUZULTQLTJIJBCYLEXSXBGQUVKEYTVQTBNRPZZRSSGOAJYKIYSHAPGLTEHKXTPFACVXOJWDNSVUNOTWIUWIYFJAGXXGWZGLKBKTFAGJFPUBNWIBCQULTMMNGHVERILEMPRDYKOLPZZNRIGDRYMMVYSGKWNAPAG"

x = decVigenere(y)
print(f'plaintext: {numToText(x)}')