# https://py.checkio.org/en/mission/bird-language/
import re 


def translation(text: str) -> str:
    words = text.split(" ")
    out_str = ""
    for word in words:
        if len(out_str):
            out_str += " "
        word = re.sub("(?<=[b-df-hj-np-tv-xz])[aeiouy]", "", word)
        word = re.sub("([aeiouy]){3}", r"\1", word)
        out_str += word
    return out_str


assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"
assert translation('aaa') == 'a'
assert translation('zy') == 'z'
assert translation('aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa') == 'abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba'
assert translation('aaaeeeiiiooouuuyyy') == 'aeiouy'
assert translation('bicydafagahajokulymonepyqarisytyvewexuzo') == 'bcdfghjklmnpqrstvwxz'
assert translation('laooorueeema iiipesiuuumo') == 'lorem ipsum'
assert translation('tyooo bieee ooora nyooote tiooo byeee') == 'to be or not to be'
assert translation('baliaaa bolaaaa boloaaa baloaaa') == 'bla bla bla bla'
assert translation('doooo yyyooouuu sapieeeaaaky eeenugaleiiisyhy') == 'do you speak english'
assert translation('iii dyooony neoooto uuunadueeerisotoaaanydy yyyooouuu') == 'i don not understand you'
