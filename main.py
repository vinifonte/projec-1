from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()




class ScreenHarmonicoMaiorNatural(Screen):

    def achar(self):
        a1 = str(self.ids.chm.text)
        if (a1 == "C") or (a1 == "c"):
            self.ids.resposta.text = a1 + ' =|I-C|II-Dm|III-Em|IV-F|V-G|VI-Am|VII-B°|'
        elif (a1 == "D") or (a1 == "d"):
            self.ids.resposta.text = a1 + " =|I-D|II-Em|III-F#m|IV-G|V-A|VI-Bm|VII-C#m5-|"
        elif (a1 == "E") or (a1 == "e"):
            self.ids.resposta.text = a1 + ' =|I-E|II-F#m|III-G#m|IV-A|V-B|VI-C#m|VII-D#m5-|'
        elif (a1 == "F") or (a1 == "f"):
            self.ids.resposta.text = a1 + ' =|I-F|II-Gm|III-Am|IV-Bb|V-C|VI-Dm|VII-Em5-|'
        elif (a1 == "G") or (a1 == "g"):
            self.ids.resposta.text = a1 + ' =|I-G|II-Am|III-Bm|IV-C|V-D|VI-Em|VII-F#m5-|'
        elif (a1 == "A") or (a1 == "a"):
            self.ids.resposta.text = a1 + ' =|I-A|II-Bm|III-C#m|IV-D|V-E|VI-F#m|VII-G#m5-|'
        elif (a1 == "B") or (a1 == "b"):
            self.ids.resposta.text = a1 + ' =|I-B|II-C#m|III-D#m|IV-E|V-F#|VI-G#m|VII-A#m5-|'
        elif (a1 == "Cb") or (a1 == "cb"):
            self.ids.resposta.text = a1 + ' =|I-Cb|II-Dbm|III-Ebm|IV-Fb|V-Gb|VI-Abm|VII-Bbm5-|'
        elif (a1 == "Db") or (a1 == "db"):
            self.ids.resposta.text = a1 + ' =|I-Db|II-Ebm|III-Fm|IV-Gb|V-Ab|VI-Bbm|VII-C°|'
        elif (a1 == "Eb") or (a1 == "eb"):
            self.ids.resposta.text = a1 + ' =|I-Eb|II-Fm|III-Gm|IV-Ab|V-Bb|VI-Cm|VII-Dm5-|'
        elif (a1 == "Gb") or (a1 == "gb"):
            self.ids.resposta.text = a1 + ' =|I-Gb|II-Abm|III-Bbm|IV-Cb|V-Db|VI-Ebm|VII-Fm5-|'
        elif (a1 == "Ab") or (a1 == "ab"):
            self.ids.resposta.text = a1 + ' =|I-Ab|II-Bbm|III-Cm|IV-Db|V-Eb|VI-Fm|VII-Gm5-|'
        elif (a1 == "Bb") or (a1 == "bb"):
            self.ids.resposta.text = a1 + ' =|I-Bb|II-Cm|III-Dm|IV-Eb|V-F|VI-Gm|VII-Am5-|'
        elif (a1 == "C#") or (a1 == "c#"):
            self.ids.resposta.text = a1 + ' =|I-C#|II-D#m|III-E#m|IV-F#|V-G#|VI-A#m|VII-B#m5-°|'
        elif (a1 == "F#") or (a1 == "f#"):
            self.ids.resposta.text = a1 + ' =|I-F#|II-G#m|III-A#m|IV-B|V-C#|VI-D#m|VII-E#m5-|'
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex: C ou Eb ou C# ...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="Os acordes formados no campo harmônico maior sempre seguirão a ordem:\n1º grau: "
                                    "sempre maior.\n2º grau: sempre menor.\n3º grau: sempre menor.\n4º grau: sempre "
                                    "maior.\n5º grau: sempre maior.\n6º grau: sempre menor.\n7º grau: sempre meio "
                                    "diminuto.",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenHarmonicoMenorNatural(Screen):

    def achar(self):
        a1 = str(self.ids.chme.text)
        if (a1 == "Cm") or (a1 == "cm"):
            self.ids.resposta.text = a1 + ' =|I-Cm|II-Dm5-|III-Eb|IV-Fm|V-Gm|VI-Ab|VII-Bb|'
        elif (a1 == "Dm") or (a1 == "dm"):
            self.ids.resposta.text = a1 + " =|I-Dm|II-Em5-|III-F|IV-Gm|V-Am|VI-Bb|VII-C|"
        elif (a1 == "Em") or (a1 == "em"):
            self.ids.resposta.text = a1 + ' =|I-Em|II-F#m5-|III-G|IV-Am|V-Bm|VI-C|VII-D|'
        elif (a1 == "Fm") or (a1 == "fm"):
            self.ids.resposta.text = a1 + ' =|I-Fm|II-Gm5-|III-Ab|IV-Bbm|V-Cm|VI-Db|VII-Eb|'
        elif (a1 == "Gm") or (a1 == "gm"):
            self.ids.resposta.text = a1 + ' =|I-Gm|II-Am5-|III-Bb|IV-Cm|V-Dm|VI-Eb|VII-F|'
        elif (a1 == "Am") or (a1 == "am"):
            self.ids.resposta.text = a1 + ' =|I-Am|II-Bm5-|III-C|IV-Dm|V-Em|VI-F|VII-G|'
        elif (a1 == "Bm") or (a1 == "bm"):
            self.ids.resposta.text = a1 + ' =|I-Bm|II-C#m5-|III-D|IV-Em|V-F#m|VI-G|VII-A|'
        elif (a1 == "C#m") or (a1 == "c#m"):
            self.ids.resposta.text = a1 + ' =|I-C#m|II-D#m5-|III-E|IV-F#m|V-G#m|VI-A|VII-B|'
        elif (a1 == "D#m") or (a1 == "d#m"):
            self.ids.resposta.text = a1 + ' =|I-D#m|II-E#m5-|III-F#|IV-G#m|V-A#m|VI-B|VII-C#|'
        elif (a1 == "Ebm") or (a1 == "ebm"):
            self.ids.resposta.text = a1 + ' =|I-Ebm|II-Fm5-|III-Gb|IV-Abm|V-Bbm|VI-Cb|VII-Db|'
        elif (a1 == "G#m") or (a1 == "g#m"):
            self.ids.resposta.text = a1 + ' =|I-G#m|II-A#m5-|III-B|IV-C#m|V-D#m|VI-E|VII-F#|'
        elif (a1 == "Abm") or (a1 == "abm"):
            self.ids.resposta.text = a1 + ' =|I-Abm|II-Bbm5-|III-Cb|IV-Dbm|V-Ebm|VI-Fb|VII-Gb|'
        elif (a1 == "Bbm") or (a1 == "bbm"):
            self.ids.resposta.text = a1 + ' =|I-Bbm|II-Cm5-|III-Db|IV-Ebm|V-Fm|VI-Gb|VII-Ab|'
        elif (a1 == "A#m") or (a1 == "a#m"):
            self.ids.resposta.text = a1 + ' =|I-A#m|II-B#m5-|III-C#|IV-D#m|V-E#m|VI-F#|VII-G#|'
        elif (a1 == "F#m") or (a1 == "f#m"):
            self.ids.resposta.text = a1 + ' =|I-F#m|II-G#m5-|III-A|IV-Bm|V-C#m|VI-D|VII-E|'
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex: Ebm ou Dm ou C#m ...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="Os acordes formados no campo harmônico menor sempre seguirão a ordem:\n1º grau: "
                                    "sempre menor.\n2º grau: sempre tipo diminuto.\n3º grau: sempre maior.\n4º grau: "
                                    "sempre"
                                    "menor.\n5º grau: sempre menor.\n6º grau: sempre maior.\n7º grau: sempre "
                                    "maior.",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()
class ScreenHarmonicoMenorHarmonica(Screen):

    def achar(self):
        a1 = str(self.ids.chmehar.text)
        if (a1 == "Cm") or (a1 == "cm"):
            self.ids.resposta.text = a1 + ' =|I-Cm|II-D°|III-Eb+|IV-Fm|V-G|VI-Ab|VII-B°|'
        elif (a1 == "Dm") or (a1 == "dm"):
            self.ids.resposta.text = a1 + " =|I-Dm|II-E°|III-F+|IV-Gm|V-A|VI-Bb|VII-C#°|"
        elif (a1 == "Em") or (a1 == "em"):
            self.ids.resposta.text = a1 + ' =|I-Em|II-F#°|III-G+|IV-Am|V-B|VI-C|VII-D#°|'
        elif (a1 == "Fm") or (a1 == "fm"):
            self.ids.resposta.text = a1 + ' =|I-Fm|II-G°|III-Ab+|IV-Bbm|V-C|VI-Db|VII-E°|'
        elif (a1 == "Gm") or (a1 == "gm"):
            self.ids.resposta.text = a1 + ' =|I-Gm|II-A°|III-Bb+|IV-Cm|V-D|VI-Eb|VII-F#°|'
        elif (a1 == "Am") or (a1 == "am"):
            self.ids.resposta.text = a1 + ' =|I-Am|II-B°|III-C+|IV-Dm|V-E|VI-F|VII-G#°|'
        elif (a1 == "Bm") or (a1 == "bm"):
            self.ids.resposta.text = a1 + ' =|I-Bm|II-C#°|III-D+|IV-Em|V-F#|VI-G|VII-A#°|'
        elif (a1 == "C#m") or (a1 == "c#m"):
            self.ids.resposta.text = a1 + ' =|I-C#m|II-D#°|III-E+|IV-F#m|V-G#|VI-A|VII-B#°|'
        elif (a1 == "D#m") or (a1 == "d#m"):
            self.ids.resposta.text = a1 + ' =|I-D#m|II-E#°|III-F#+|IV-G#m|V-A#|VI-B|VII-Cx°(D°)|'
        elif (a1 == "Ebm") or (a1 == "ebm"):
            self.ids.resposta.text = a1 + ' =|I-Ebm|II-F°|III-Gb+|IV-Abm|V-Bb|VI-Cb|VII-D°|'
        elif (a1 == "G#m") or (a1 == "g#m"):
            self.ids.resposta.text = a1 + ' =|I-G#m|II-A#°|III-B+|IV-C#m|V-D#|VI-E|VII-Fx°(G°)|'
        elif (a1 == "Abm") or (a1 == "abm"):
            self.ids.resposta.text = a1 + ' =|I-Abm|II-Bb°|III-Cb+|IV-Dbm|V-Eb|VI-Fb|VII-G°|'
        elif (a1 == "Bbm") or (a1 == "bbm"):
            self.ids.resposta.text = a1 + ' =|I-Bbm|II-C°|III-Db+|IV-Ebm|V-F|VI-Gb|VII-A°|'
        elif (a1 == "A#m") or (a1 == "a#m"):
            self.ids.resposta.text = a1 + ' =|I-A#m|II-B#°|III-C#+|IV-D#m|V-E#|VI-F#|VII-Gx°(A°)|'
        elif (a1 == "F#m") or (a1 == "f#m"):
            self.ids.resposta.text = a1 + ' =|I-F#m|II-G#°|III-A+|IV-Bm|V-C#|VI-D|VII-E#°|'
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex: Ebm ou Dm ou C#m ...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="Os acordes formados no campo harmônico menor harmônica sempre seguirão a "
                                    "ordem:\n1º grau:"
                                    "sempre menor.\n2º grau: sempre diminuto.\n3º grau: sempre aumentado.\n4º grau: "
                                    "sempre"
                                    "menor.\n5º grau: sempre maior.\n6º grau: sempre maior.\n7º grau: sempre "
                                    "diminuto.",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenHarmonicoMenorMelodico(Screen):
    def achar(self):
        a1 = str(self.ids.chmemel.text)
        if (a1 == "Cm") or (a1 == "cm"):
            self.ids.resposta.text = a1 + ' =|I-Cm|II-Dm|III-Eb+|IV-F|V-G|VI-A°|VII-B°|'
        elif (a1 == "Dm") or (a1 == "dm"):
            self.ids.resposta.text = a1 + " =|I-Dm|II-Em|III-F+|IV-G|V-A|VI-B°|VII-C#°|"
        elif (a1 == "Em") or (a1 == "em"):
            self.ids.resposta.text = a1 + ' =|I-Em|II-F#m|III-G+|IV-A|V-B|VI-C#°|VII-D#°|'
        elif (a1 == "Fm") or (a1 == "fm"):
            self.ids.resposta.text = a1 + ' =|I-Fm|II-Gm|III-Ab+|IV-Bb|V-C|VI-D°|VII-E°|'
        elif (a1 == "Gm") or (a1 == "gm"):
            self.ids.resposta.text = a1 + ' =|I-Gm|II-Am|III-Bb+|IV-C|V-D|VI-E°|VII-F#°|'
        elif (a1 == "Am") or (a1 == "am"):
            self.ids.resposta.text = a1 + ' =|I-Am|II-Bm|III-C+|IV-D|V-E|VI-F#°|VII-G#°|'
        elif (a1 == "Bm") or (a1 == "bm"):
            self.ids.resposta.text = a1 + ' =|I-Bm|II-C#m|III-D+|IV-E|V-F#|VI-G#°|VII-A#°|'
        elif (a1 == "C#m") or (a1 == "c#m"):
            self.ids.resposta.text = a1 + ' =|I-C#m|II-D#m|III-E+|IV-F#|V-G#|VI-A#°|VII-B#°|'
        elif (a1 == "D#m") or (a1 == "d#m"):
            self.ids.resposta.text = a1 + ' =|I-D#m|II-E#m|III-F#+|IV-G#|V-A#|VI-B#°|VII-Cx°(D°)|'
        elif (a1 == "Ebm") or (a1 == "ebm"):
            self.ids.resposta.text = a1 + ' =|I-Ebm|II-Fm|III-Gb+|IV-Ab|V-Bb|VI-C°|VII-D°|'
        elif (a1 == "G#m") or (a1 == "g#m"):
            self.ids.resposta.text = a1 + ' =|I-G#m|II-A#m|III-B+|IV-C#|V-D#|VI-E#°|VII-Fx°(G°)|'
        elif (a1 == "Abm") or (a1 == "abm"):
            self.ids.resposta.text = a1 + ' =|I-Abm|II-Bbm|III-Cb+|IV-Db|V-Eb|VI-F°|VII-G°|'
        elif (a1 == "Bbm") or (a1 == "bbm"):
            self.ids.resposta.text = a1 + ' =|I-Bbm|II-Cm|III-Db+|IV-Eb|V-F|VI-G°|VII-A°|'
        elif (a1 == "A#m") or (a1 == "a#m"):
            self.ids.resposta.text = a1 + ' =|I-A#m|II-B#m|III-C#+|IV-D#|V-E#|VI-F#°|VII-Gx°(A°)|'
        elif (a1 == "F#m") or (a1 == "f#m"):
            self.ids.resposta.text = a1 + ' =|I-F#m|II-G#m|III-A+|IV-B|V-C#|VI-D#°|VII-E#°|'
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex: Ebm ou Dm ou C#m ...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="Os acordes formados no campo harmônico menor melódico sempre seguirão a "
                                    "ordem:\n1º grau:"
                                    "sempre menor.\n2º grau: sempre menor.\n3º grau: sempre aumentado.\n4º grau: sempre"
                                    "maior.\n5º grau: sempre maior.\n6º grau: sempre diminuto.\n7º grau: sempre "
                                    "diminuto.",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenEscalaMaiorNatural(Screen):

    def achar(self):
        e1 = str(self.ids.esmanat.text)
        if (e1 == "C") or (e1 == "c"):
            self.ids.resposta.text = e1 + ' =|I-C|II-D|III-E|IV-F|V-G|VI-A|VII-B|'
        elif (e1 == "D") or (e1 == "d"):
            self.ids.resposta.text = e1 + " =|I-D|II-E|III-F#|IV-G|V-A|VI-B|VII-C#|"
        elif (e1 == "E") or (e1 == "e"):
            self.ids.resposta.text = e1 + " =|I-E|II-F#|III-G#|IV-A|V-B|VI-C#|VII-D#|"
        elif (e1 == "F") or (e1 == "f"):
            self.ids.resposta.text = e1 + " =|I-F|II-G|III-A|IV-Bb|V-C|VI-D|VII-E|"
        elif (e1 == "G") or (e1 == "g"):
            self.ids.resposta.text = e1 + " =|I-G|II-A|III-B|IV-C|V-D|VI-E|VII-F#|"
        elif (e1 == "A") or (e1 == "a"):
            self.ids.resposta.text = e1 + " =|I-A|II-B|III-C#|IV-D|V-E|VI-F#|VII-G#|"
        elif (e1 == "B") or (e1 == "b"):
            self.ids.resposta.text = e1 + " =|I-B|II-C#|III-D#|IV-E|V-F#|VI-G#|VII-Bb|"
        elif (e1 == "C#") or (e1 == "c#"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E#|IV-F#|V-G#|VI-A#|VII-C|"
        elif (e1 == "D#") or (e1 == "d#"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-F|III-G|IV-Ab|V-Bb|VI-C|VII-D|"
        elif (e1 == "F#") or (e1 == "f#"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-Bb|IV-B|V-C#|VI-D#|VII-F|"
        elif (e1 == "G#") or (e1 == "g#"):
            self.ids.resposta.text = e1 + " =|I-Ab|II-Bb|III-C|IV-Db|V-Eb|VI-F|VII-G|"
        elif (e1 == "A#") or (e1 == "a#"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-D|IV-Eb|V-F|VI-G|VII-A|"
        elif (e1 == "Db") or (e1 == "db"):
            self.ids.resposta.text = e1 + " =|I-Db|II-Eb|III-F|IV-Gb|V-Ab|VI-Bb|VII-C|"
        elif (e1 == "Eb") or (e1 == "eb"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-F|III-G|IV-Ab|V-Bb|VI-C|VII-D|"
        elif (e1 == "Gb") or (e1 == "gb"):
            self.ids.resposta.text = e1 + " =|I-Gb|II-Ab|III-Bb|IV-Cb|V-Db|VI-Eb|VII-F|"
        elif (e1 == "Ab") or (e1 == "ab"):
            self.ids.resposta.text = e1 + " =|I-Ab|II-Bb|III-C|IV-Db|V-Eb|VI-F|VII-G|"
        elif (e1 == "Bb") or (e1 == "bb"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-D|IV-Eb|V-F|VI-G|VII-A|"
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex:C ou Db ou F#...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="É formada pelos seguintes intervalos: tônica, segunda maior, terça"
                                    "\nmaior, quarta justa, quinta justa, sexta maior, sétima maior. ",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenEscalaMenorNatural(Screen):
    def achar(self):
        e1 = str(self.ids.esmenat.text)
        if (e1 == "C") or (e1 == "c"):
            self.ids.resposta.text = e1 + ' =|I-C|II-D|III-Eb|IV-F|V-G|VI-Ab|VII-Bb|'
        elif (e1 == "D") or (e1 == "d"):
            self.ids.resposta.text = e1 + " =|I-D|II-E|III-F|IV-G|V-A|VI-Bb|VII-C|"
        elif (e1 == "E") or (e1 == "e"):
            self.ids.resposta.text = e1 + " =|I-E|II-F#|III-G|IV-A|V-B|VI-C|VII-D|"
        elif (e1 == "F") or (e1 == "f"):
            self.ids.resposta.text = e1 + " =|I-F|II-G|III-Ab|IV-Bb|V-C|VI-Db|VII-Eb|"
        elif (e1 == "G") or (e1 == "g"):
            self.ids.resposta.text = e1 + " =|I-G|II-A|III-Bb|IV-C|V-D|VI-Eb|VII-F|"
        elif (e1 == "A") or (e1 == "a"):
            self.ids.resposta.text = e1 + " =|I-A|II-B|III-C|IV-D|V-E|VI-F|VII-G|"
        elif (e1 == "B") or (e1 == "b"):
            self.ids.resposta.text = e1 + " =|I-B|II-C#|III-D|IV-E|V-F#|VI-G|VII-A|"
        elif (e1 == "C#") or (e1 == "c#"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E|IV-F#|V-G#|VI-A|VII-B|"
        elif (e1 == "D#") or (e1 == "d#"):
            self.ids.resposta.text = e1 + " =|I-D#|II-E#|III-F#|IV-G#|V-A#|VI-B|VII-C#|"
        elif (e1 == "F#") or (e1 == "f#"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-A|IV-B|V-C#|VI-D|VII-E|"
        elif (e1 == "G#") or (e1 == "g#"):
            self.ids.resposta.text = e1 + " =|I-G#|II-Bb|III-B|IV-C#|V-D#|VI-E|VII-F#|"
        elif (e1 == "A#") or (e1 == "a#"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-Db|IV-Eb|V-F|VI-Gb|VII-Ab|"
        elif (e1 == "Db") or (e1 == "db"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E|IV-F#|V-G#|VI-A|VII-B|"
        elif (e1 == "Eb") or (e1 == "eb"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-F|III-Gb|IV-Ab|V-Bb|VI-Cb|VII-Db|"
        elif (e1 == "Gb") or (e1 == "gb"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-A|IV-B|V-C#|VI-D|VII-E|"
        elif (e1 == "Ab") or (e1 == "ab"):
            self.ids.resposta.text = e1 + " =|I-G#|II-Bb|III-B|IV-C#|V-D#|VI-E|VII-F#|"
        elif (e1 == "Bb") or (e1 == "bb"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-Db|IV-Eb|V-F|VI-Gb|VII-Ab|"
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex:C ou Db ou F#...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="É formada pelos seguintes intervalos: tônica, segunda maior, terça menor, "
                                    "quarta justa,"
                                    "\n quinta justa,sexta menor, sétima menor.",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenEscalaMenorHarmonica(Screen):
    def achar(self):
        e1 = str(self.ids.esmehar.text)
        if (e1 == "C") or (e1 == "c"):
            self.ids.resposta.text = e1 + ' =|I-C|II-D|III-Eb|IV-F|V-G|VI-Ab|VII-B|'
        elif (e1 == "D") or (e1 == "d"):
            self.ids.resposta.text = e1 + " =|I-D|II-E|III-F|IV-G|V-A|VI-Bb|VII-Db|"
        elif (e1 == "E") or (e1 == "e"):
            self.ids.resposta.text = e1 + " =|I-E|II-F#|III-G|IV-A|V-B|VI-C|VII-D#|"
        elif (e1 == "F") or (e1 == "f"):
            self.ids.resposta.text = e1 + " =|I-F|II-G|III-Ab|IV-Bb|V-C|VI-Db|VII-E|"
        elif (e1 == "G") or (e1 == "g"):
            self.ids.resposta.text = e1 + " =|I-G|II-A|III-Bb|IV-C|V-D|VI-Eb|VII-Gb|"
        elif (e1 == "A") or (e1 == "a"):
            self.ids.resposta.text = e1 + " =|I-A|II-B|III-C|IV-D|V-E|VI-F|VII-G#|"
        elif (e1 == "B") or (e1 == "b"):
            self.ids.resposta.text = e1 + " =|I-B|II-C#|III-D|IV-E|V-F#|VI-G|VII-Bb|"
        elif (e1 == "C#") or (e1 == "c#"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E|IV-F#|V-G#|VI-A|VII-C|"
        elif (e1 == "D#") or (e1 == "d#"):
            self.ids.resposta.text = e1 + " =|I-D#|II-E#|III-F#|IV-G#|V-A#|VI-B|VII-D|"
        elif (e1 == "F#") or (e1 == "f#"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-A|IV-B|V-C#|VI-D|VII-F|"
        elif (e1 == "G#") or (e1 == "g#"):
            self.ids.resposta.text = e1 + " =|I-G#|II-Bb|III-B|IV-C#|V-D#|VI-E|VII-G|"
        elif (e1 == "A#") or (e1 == "a#"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-Db|IV-Eb|V-F|VI-Gb|VII-A|"
        elif (e1 == "Db") or (e1 == "db"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E|IV-F#|V-G#|VI-A|VII-C|"
        elif (e1 == "Eb") or (e1 == "eb"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-F|III-Gb|IV-Ab|V-Bb|VI-Cb|VII-D|"
        elif (e1 == "Gb") or (e1 == "gb"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-A|IV-B|V-C#|VI-D|VII-F|"
        elif (e1 == "Ab") or (e1 == "ab"):
            self.ids.resposta.text = e1 + " =|I-G#|II-Bb|III-B|IV-C#|V-D#|VI-E|VII-G|"
        elif (e1 == "Bb") or (e1 == "bb"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-Db|IV-Eb|V-F|VI-Gb|VII-A|"
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex:C ou Db ou F#...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="A escala menor harmônica é derivada da escala diatônica menor natural e ela é "
                                    "obtida"
                                    "\nelevando-se meio tom o sétimo grau. Substitui-o a sétima menor pela sétima "
                                    "maior. É formada pelos seguintes intervalos: tônica, segunda maior, terça menor, "
                                    "quarta justa,"
                                    "\nquinta justa, sexta menor, sétima maior.  ",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenEscalaMenorMelodica(Screen):
    def achar(self):
        e1 = str(self.ids.esmemel.text)
        if (e1 == "C") or (e1 == "c"):
            self.ids.resposta.text = e1 + ' =|I-C|II-D|III-Eb|IV-F|V-G|VI-A|VII-B|'
        elif (e1 == "D") or (e1 == "d"):
            self.ids.resposta.text = e1 + " =|I-D|II-E|III-F|IV-G|V-A|VI-B|VII-C#|"
        elif (e1 == "E") or (e1 == "e"):
            self.ids.resposta.text = e1 + " =|I-E|II-F#|III-G|IV-A|V-B|VI-C#|VII-D#|"
        elif (e1 == "F") or (e1 == "f"):
            self.ids.resposta.text = e1 + " =|I-F|II-G|III-Ab|IV-Bb|V-C|VI-D|VII-E|"
        elif (e1 == "G") or (e1 == "g"):
            self.ids.resposta.text = e1 + " =|I-G|II-A|III-Bb|IV-C|V-D|VI-E|VII-Gb|"
        elif (e1 == "A") or (e1 == "a"):
            self.ids.resposta.text = e1 + " =|I-A|II-B|III-C|IV-D|V-E|VI-F#|VII-G#|"
        elif (e1 == "B") or (e1 == "b"):
            self.ids.resposta.text = e1 + " =|I-B|II-C#|III-D|IV-E|V-F#|VI-G#|VII-Bb|"
        elif (e1 == "C#") or (e1 == "c#"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E|IV-F#|V-G#|VI-Bb|VII-C|"
        elif (e1 == "D#") or (e1 == "d#"):
            self.ids.resposta.text = e1 + " =|I-D#|II-E#|III-F#|IV-G#|V-A#|VI-C|VII-D|"
        elif (e1 == "F#") or (e1 == "f#"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-A|IV-B|V-C#|VI-D#|VII-F|"
        elif (e1 == "G#") or (e1 == "g#"):
            self.ids.resposta.text = e1 + " =|I-G#|II-Bb|III-B|IV-C#|V-D#|VI-F|VII-G|"
        elif (e1 == "A#") or (e1 == "a#"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-Db|IV-Eb|V-F|VI-G|VII-A|"
        elif (e1 == "Db") or (e1 == "db"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-E|IV-F#|V-G#|VI-Bb|VII-C|"
        elif (e1 == "Eb") or (e1 == "eb"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-F|III-Gb|IV-Ab|V-Bb|VI-C|VII-D|"
        elif (e1 == "Gb") or (e1 == "gb"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-A|IV-B|V-C#|VI-D#|VII-F|"
        elif (e1 == "Ab") or (e1 == "ab"):
            self.ids.resposta.text = e1 + " =|IAb|II-Bb|III-Cb|IV-Db|V-Eb|VI-F|VII-G|"
        elif (e1 == "Bb") or (e1 == "bb"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-Db|IV-Eb|V-F|VI-G|VII-A|"
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex:C ou Db ou F#...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="A escala menor melódica, também conhecida como escala menor de jazz é derivada da"
                                    "\nescala menor harmônica. O sexto grau da escala menor harmônica é elevado de um"
                                    "\nsemiton. É formada pelos seguintes intervalos: tônica, segunda maior, "
                                    "terça menor,"
                                    "\nquarta justa, quinta justa, sexta maior, sétima maior",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenEscalaPentaMaior(Screen):
    def achar(self):
        e1 = str(self.ids.espenma.text)
        if (e1 == "C") or (e1 == "c"):
            self.ids.resposta.text = e1 + ' =|I-C|II-D|III-E|IV-F|V-G|'
        elif (e1 == "D") or (e1 == "d"):
            self.ids.resposta.text = e1 + " =|I-D|II-E|III-F#|IV-A|V-B|"
        elif (e1 == "E") or (e1 == "e"):
            self.ids.resposta.text = e1 + " =|I-E|II-F#|III-G#|IV-B|V-C#|"
        elif (e1 == "F") or (e1 == "f"):
            self.ids.resposta.text = e1 + " =|I-F|II-G|III-A|IV-C|V-D|"
        elif (e1 == "G") or (e1 == "g"):
            self.ids.resposta.text = e1 + " =|I-G|II-A|III-B|IV-D|V-E|"
        elif (e1 == "A") or (e1 == "a"):
            self.ids.resposta.text = e1 + " =|I-A|II-B|III-C#|IV-E|V-F#|"
        elif (e1 == "B") or (e1 == "b"):
            self.ids.resposta.text = e1 + " =|I-B|II-C#|III-D#|IV-F#|V-G#|"
        elif (e1 == "C#") or (e1 == "c#"):
            self.ids.resposta.text = e1 + " =|I-C#|II-D#|III-F|IV-G#|V-Bb|"
        elif (e1 == "D#") or (e1 == "d#"):
            self.ids.resposta.text = e1 + " =|I-D#|II-F|III-G|IV-Bb|V-C|"
        elif (e1 == "F#") or (e1 == "f#"):
            self.ids.resposta.text = e1 + " =|I-F#|II-G#|III-Bb|IV-C#|V-D#|"
        elif (e1 == "G#") or (e1 == "g#"):
            self.ids.resposta.text = e1 + " =|I-G#|II-Bb|III-C|IV-D#|V-F|"
        elif (e1 == "A#") or (e1 == "a#"):
            self.ids.resposta.text = e1 + " =|I-A#|II-C|III-D|IV-E#|V-G|"
        elif (e1 == "Db") or (e1 == "db"):
            self.ids.resposta.text = e1 + " =|I-Db|II-Eb|III-F|IV-Ab|V-Bb|"
        elif (e1 == "Eb") or (e1 == "eb"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-F|III-G|IV-Bb|V-C|"
        elif (e1 == "Gb") or (e1 == "gb"):
            self.ids.resposta.text = e1 + " =|I-Gb|II-Ab|III-Bb|IV-Db|V-Eb|"
        elif (e1 == "Ab") or (e1 == "ab"):
            self.ids.resposta.text = e1 + " =|I-Ab|II-Bb|III-C|IV-Eb|V-F|"
        elif (e1 == "Bb") or (e1 == "bb"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-C|III-D|IV-F|V-G|"
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex:C ou Db ou F#...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="Possui cinco notas, e é obtida através da escala diatônica maior natural, "
                                    "eliminando os"
                                    "\nintervalos de quarta justa e sétima maior."
                                    "\nÉ formada pelos intervalos: tônica, segunda maior, terça maior, quinta justa, "
                                    "sexta"
                                    "\nmaior.",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class ScreenEscalaPentaMenor(Screen):
    def achar(self):
        e1 = str(self.ids.espenme.text)
        if (e1 == "C") or (e1 == "c"):
            self.ids.resposta.text = e1 + " =|I-C|II-D#|III-F|IV-G|V-Bb|"
        elif (e1 == "D") or (e1 == "d"):
            self.ids.resposta.text = e1 + " =|I-D|II-F|III-G|IV-A|V-C|"
        elif (e1 == "E") or (e1 == "e"):
            self.ids.resposta.text = e1 + " =|I-E|II-G|III-A|IV-B|V-D|"
        elif (e1 == "F") or (e1 == "f"):
            self.ids.resposta.text = e1 + " =|I-F|II-G#|III-Bb|IV-C|V-D#|"
        elif (e1 == "G") or (e1 == "g"):
            self.ids.resposta.text = e1 + " =|I-G|II-A#|III-C|IV-D|V-E#|"
        elif (e1 == "A") or (e1 == "a"):
            self.ids.resposta.text = e1 + " =|I-A|II-C|III-D|IV-E|V-G|"
        elif (e1 == "B") or (e1 == "b"):
            self.ids.resposta.text = e1 + " =|I-B|II-D|III-E|IV-F#|V-A|"
        elif (e1 == "C#") or (e1 == "c#"):
            self.ids.resposta.text = e1 + " =|I-C#|II-E|III-F#|IV-G#|V-B|"
        elif (e1 == "D#") or (e1 == "d#"):
            self.ids.resposta.text = e1 + " =|I-D#|II-F#|III-G#|IV-Bb|V-C#|"
        elif (e1 == "F#") or (e1 == "f#"):
            self.ids.resposta.text = e1 + " =|I-F#|II-A|III-B|IV-C#|V-E|"
        elif (e1 == "G#") or (e1 == "g#"):
            self.ids.resposta.text = e1 + " =|I-G#|II-B|III-C#|IV-D#|V-F#|"
        elif (e1 == "A#") or (e1 == "a#"):
            self.ids.resposta.text = e1 + " =|I-A#|II-C#|III-D#|IV-E#|V-G#|"
        elif (e1 == "Db") or (e1 == "db"):
            self.ids.resposta.text = e1 + " =|I-Db|II-E|III-Gb|IV-Ab|V-B|"
        elif (e1 == "Eb") or (e1 == "eb"):
            self.ids.resposta.text = e1 + " =|I-Eb|II-Gb|III-Ab|IV-Bb|V-Db|"
        elif (e1 == "Gb") or (e1 == "gb"):
            self.ids.resposta.text = e1 + " =|I-Gb|II-A|III-B|IV-Db|V-E|"
        elif (e1 == "Ab") or (e1 == "ab"):
            self.ids.resposta.text = e1 + " =|I-Ab|II-B|III-Db|IV-Eb|V-Gb|"
        elif (e1 == "Bb") or (e1 == "bb"):
            self.ids.resposta.text = e1 + " =|I-Bb|II-Db|III-Eb|IV-F|V-Ab|"
        else:
            self.ids.resposta.text = 'Dado Incorreto!Digite ->Ex:C ou Db ou F#...'

    def dicas(self):
        self.dialog = MDDialog(title='DICA',
                               text="Possui cinco notas, e é obtida através da escala diatônica menor natural, "
                                    "eliminando os"
                                    "\nintervalos de segunda maior e sexta menor."
                                    "\nÉ formada pelos seguintes intervalos: tônica, terça menor, quarta justa, "
                                    "quinta justa,"
                                    "\nsétima menor. ",
                               buttons=[MDFlatButton(text='Ok',
                                                     on_release=self.liberar)])
        self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()

class NotasMusicaisPlus(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')


NotasMusicaisPlus().run()
