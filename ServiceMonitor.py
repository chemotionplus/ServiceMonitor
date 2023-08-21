#<!-- /////////                                                             /////////
#    //////////////                                                     //////////////
#    /////////////////                                               /////////////////
#    ////////////////////                                         ////////////////////
#    //////////////////////            (((((///(((((            //////////////////////
#    ////////////////////////(((((((//((((((///((((((//(((((((////////////////////////
#     //////////////////((((((((((((((((((((///((((((((((((((((((((//////////////////
#     //////////////((((((((((((((((((/((((((/((((((/((((((((((((((((((//////////////
#      /////////((((((((((((((((((((///(((((((((((((///((((((((((((((((((((/////////
#      ///////(((((((((((((((((((((/(//(((((((((((((/((/(((((((((((((((((((((///////
#       ////((((((((((((((((((((((/(((/(((((((((((((/(((/((((((((((((((((((((((////
#        /((((((((((((((((((((((((/((((//(((((((((//((((/((((((((((((((((((((((((/
#       (((((((((((((((((((((((((//((((((//(((((//((((((//(((((((((((((((((((((((((
#      (((((((((((((((((((((((((((/(((((((((((((((((((((/(((((((((((((((((((((((((((
#     ((((((((((((((((((((((((((((/(((((((((((((((((((((/((((((((((((((((((((((((((((
#     (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#    ////////////((((((/&******//(((((((((((((((((((((((((//******@/(((((/////////////
#    ///////(((((((((%@*****@ ***//(((((((((%%%(((((((((/**** @*****@/((((((((((//////
#    (((((((((((((((((@****  *****/(((((((%%%%%%%(((((((#*****  ****@(((((((((((((((((
#    ////////////////((@@********@(((((%%%%%%%%%%%%%((((&@********@@(/////////////////
#     (((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%(((((((((((((((((((((((((((((
#     (%%%%#((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%((((((((((((((((((#%%%%%
#      %%%%%%%%%%##########%%%%%%%%%%%%%%@#######&%%%%%%%%%%%%%%##########%%%%%%%%%%
#       ,%%%%%%%%##########%%%%%%%%%%@@@@#########@@@@%%%%%%%%%%##########%%%%%%%%%
#         %%%%%%%%##%%####%%&@&&%%%%@@@@@@%#####@@@@@@@%%%%&&@&%%####%###%%%%%%%%
#         @ %%%%%%%%%%%%%%&%%%%%&%%%@@@@@@@@###@@@@@@@@%%%&%%%%%&%%%%%%%%%%%%%% @
#   &      @ @%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@ @@@@@@@@%%%%%%%%%%%%%%%%%%%%&%%@ @ (    /
#                %%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%
#                   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                           //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%//          //   //
#                               /////////#%%%%%%%%/////////          /*///// ///// /
#                                      ////////////.               / // *////////,//
#                                                                   //////////
#                                                                   ///// //////©chemotionplus 2023
#                                                                  ///////////// ,//
#                                                                     ///  /// /////
#                                                                      // ///// / -->
import socket
import time
import argparse
import signal
import sys

# Fonction de gestion de l'interruption (Ctrl+C)
def signal_handler(sig, frame):
    sys.exit(0)

# Définir la fonction de gestion de l'interruption
signal.signal(signal.SIGINT, signal_handler)

# Définir les arguments en ligne de commande
parser = argparse.ArgumentParser(description="Test de disponibilité d'un service via son adresse IP et port.")
parser.add_argument("--ip", required=True, help="Adresse IP du service à tester.")
parser.add_argument("--port", type=int, required=True, help="Port du service à tester.")
parser.add_argument("--log", default="service_availability.log", help="Chemin vers le fichier journal.")
args = parser.parse_args()

def test_service_availability(ip, port):
    try:
        # Créer une socket pour tester la connexion
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Timeout de 5 secondes
            start_time = time.time()
            s.connect((ip, port))
            end_time = time.time()
            latency = end_time - start_time

            # Obtenir l'heure actuelle
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            # Écrire le résultat dans le fichier journal
            with open(args.log, "a") as log_file:
                log_file.write(f"[{current_time}] {ip}:{port} est disponible (latence : {latency:.4f} secondes)\n")

            print(f"[{current_time}] {ip}:{port} est disponible (latence : {latency:.4f} secondes)")
    except Exception as e:
        # Obtenir l'heure actuelle
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        # En cas d'erreur, enregistrer dans le journal
        with open(args.log, "a") as log_file:
            log_file.write(f"{ip}:{port} est indisponible (erreur : {str(e)})\n")

        print(f"[{current_time}] {ip}:{port} est indisponible (erreur : {str(e)})")

# Boucle infinie de test
while True:
    test_service_availability(args.ip, args.port)
    time.sleep(0.5)  # Temps d'attente avant de retester
