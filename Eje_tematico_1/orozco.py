cancion = """Nosotros no somos como los Orozco,
yo los conozco, son ocho los monos:
Pocho, Toto, Cholo, Tom,
Moncho, Rodolfo, Otto, Pololo.
Yo pongo los votos sólo por Rodolfo,
los otros son locos, yo los conozco, no los soporto.
Stop. Stop.

Pocho Orozco:
Odontólogo ortodoxo, doctor
Como Borocotó
Oncólogo jodón Morocho tordo
Groncho jocoso
Trosko
Chocó con los montos
Colocó Molotov. Bonzo.

Toto Orozco:
Colocón
Drogón como pocos
Tomó todos los hongos
Monologó solo como por dos otoños
Botó formol por los hongos
Tomó cloroformo, bols, ron, porrón, torronto, toso
Norto con Bordón
¿Lo votó o no?
Dobló los codos como loco
¡¡Coño!! ¿sos vos Toto?
Corroboró
Socorro, cómo tomó
Morfó hot dog, mondongo, pollo con porotos
Lloró, lloró con dolor
Por como lloró tomó como dos hongos
Tocó fondo
Tocó como loco
Contó todo, todo, todo
Bochornoso como Cóppolo. Stop. Stop.

Cholo Orozco:
Mocoso
Soplón
Moroso
Bocón
Chorro como Grosso
Robó dos potros por Comodoro,
los montó, los trotó por Bolsón,
por los Toldos,
por Chocón
Doloroso. Stop. Stop.

Tom Orozco:
Proctólogo morboso
Compró por los shops fotos porno color
Compró como dos tomos
Trozos
Cosos
Colchón roto
Homós como Gomón
Trolos gozosos con condón
Pomos con moño rococó
Todos polvos cortos
Fogoso. Stop. Stop.

Nosotros no somos como los Orozco,
yo los conozco, son ocho los monos:
Pocho, Toto, Cholo, Tom,
Moncho, Rodolfo, Otto, Pololo.
Yo pongo los votos sólo por Rodolfo,
los otros son locos, yo los conozco, no los soporto.
Stop. Stop.

Moncho Orozco:
Sólo probó porro
Voló con los ojos rojos por los polos
Voló por Bonn, voló por Hong Kong
Por London, soñó con Yoko Ono, lloró por John
Voló por vos
Voló por nosotros
Brotó como flor bordó
Roló pot, nos contó
Los tronchos son grosos como los corchos
Bocho borroso. Stop. Stop.

Rodolfo Orozco:
Con voz como John Scott
Ronco, ronco
Formó todos los coros
Tocó: Doblo con Mollo, bombo con Moro,
tom tom con Porno, joropo con Tormo, bongó con Don Johnson
Tocó con Toto, los Lobos, los Door, los Moscos
Compró dos vox
Tocó "Socorro" con Pol
Nos contó con honor: ¡Toco con Bob! ¡Toco con Bob!
Sopló corno, trombón
Tocó son sonoro con los cocos
Rock, pop, folk, pogo
Nos contó como oyó todos los: ¡¡Oh, oh, oh, oh, oh... !!
Tocó con todos
Por poco no tocó con Colón
Coloso. Stop. Stop.

Otto Orozco:
Con otros rollos
Con poco protocolo
Copó todo como los Born, Troncoso, Don Floro o los Lococo
Logró otro comfort
Ojo por ojo
Controló todo
Convocó por fono los otros Orozco
Contó con todos
Cobró todos los bonos
Bocón
Colocó montos grosos por Boston
Cobró dos lotos
Compró dos Ford, ocho Volvo, dos Gol
Oro
Motos
Toros
Compró los Coto, Rodó, Coconor
Zorro. Stop. Stop.

Pololo Orozco:
Gordo fofo con olor
Mormón
Glotón con jopo
Rostro poroso
Rotoso
Como con motor roto
Solo como croto
Solo como topo
Solo como Don Bosco con poncho
Choto. Stop. Stop."""

def contar(letra, cancion):
    cont = 0
    for l in cancion:
        if l == letra:
            cont += 1
    return cont

letra = input("Ingrese la letra a contar: ")

print(f"La letra {letra} aparece {contar(letra,cancion)} veces.")
