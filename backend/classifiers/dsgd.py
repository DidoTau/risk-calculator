from DSGD.DSClassifierMultiQ import DSClassifierMultiQ
import pandas as pd


class DSGDClassifier:
    # create a DSGD classifier with class = 2,min_iter=1, max_iter=200, min_dloss=0.0001,debug_mode=True, num_workers=4, lossfn="MSE", optim="adam", precompute_rules=True, lr=0.001
    def __init__(self, class_num=2, min_iter=1, max_iter=200, min_dloss=0.0001, debug_mode=True, num_workers=4, lossfn="MSE", optim="adam", precompute_rules=True, lr=0.001):

        self.dsgd = DSClassifierMultiQ(class_num, min_iter, max_iter, min_dloss,
                                       debug_mode, num_workers, lossfn, optim, precompute_rules, lr)

    def load_rules(self, rules):
        self.dsgd.model.load_rules(rules)

    def preprocessing(self, input_data):
        processed_data = pd.DataFrame()
        input_data = pd.DataFrame(input_data)
        # preprocess the data following ['edad',
        # 'status_menop_al_dg_MENOPAUSICA',
        #    'status_menop_al_dg_NO SE MENCIONA',
        #    'status_menop_al_dg_POSTMENOPAUSICA',
        #    'status_menop_al_dg_PREMENOPAUSICA', 'imc', 'ct_cT1', 'ct_cT2',
        #    'ct_cT3', 'ct_cT4', 'cn_cN0', 'cn_cN1', 'cn_cN2', 'cn_cN3', 'etapa_I',
        #    'etapa_II', 'etapa_III', 'axila_en_eco', 'tipo_histologico_CDI',
        #    'tipo_histologico_CI', 'tipo_histologico_CLI',
        #    'tipo_histologico_No concluyente', 're', 'rp', 'ki67',
        #    'relacion_her_2_cen', 'n°_de_copias', 'perfil_molecular', 'esquema',

        processed_data["age"] = input_data["age"]
        # passing a boolean to 0 or 1
        def boolean_to_int(x): return 1 if x else 0
        processed_data["status_menop_al_dg_MENOPAUSICA"] = boolean_to_int(
            input_data["status_menop"] == 0)
        processed_data["status_menop_al_dg_NO SE MENCIONA"] = boolean_to_int(
            input_data["status_menop"] == 1)
        processed_data["status_menop_al_dg_POSTMENOPAUSICA"] = boolean_to_int(
            input_data["status_menop"] == 2)
        processed_data["status_menop_al_dg_PREMENOPAUSICA"] = boolean_to_int(
            input_data["status_menop"] == 3)
        processed_data["imc"] = input_data["imc"]
        processed_data["ct_cT1"] = boolean_to_int(input_data["ct"] == 0)
        processed_data["ct_cT2"] = boolean_to_int(input_data["ct"] == 1)
        processed_data["ct_cT3"] = boolean_to_int(input_data["ct"] == 2)
        processed_data["ct_cT4"] = boolean_to_int(input_data["ct"] == 3)
        processed_data["cn_cN0"] = boolean_to_int(input_data["cn"] == 0)
        processed_data["cn_cN1"] = boolean_to_int(input_data["cn"] == 1)
        processed_data["cn_cN2"] = boolean_to_int(input_data["cn"] == 2)
        processed_data["cn_cN3"] = boolean_to_int(input_data["cn"] == 3)
        processed_data["etapa_I"] = boolean_to_int(input_data["stage"] == 0)
        processed_data["etapa_II"] = boolean_to_int(input_data["stage"] == 1)
        processed_data["etapa_III"] = boolean_to_int(input_data["stage"] == 2)
        processed_data["axila_en_eco"] = input_data["axila_en_eco"]
        processed_data["tipo_histologico_CDI"] = boolean_to_int(
            input_data["tipo_histologico"] == 0)
        processed_data["tipo_histologico_CI"] = boolean_to_int(
            input_data["tipo_histologico"] == 1)
        processed_data["tipo_histologico_CLI"] = boolean_to_int(
            input_data["tipo_histologico"] == 2)
        processed_data["tipo_histologico_No concluyente"] = boolean_to_int(
            input_data["tipo_histologico"] == 3)
        processed_data["re"] = input_data["re"]
        processed_data["rp"] = input_data["rp"]
        processed_data["ki67"] = input_data["ki67"]
        processed_data["relacion_her_2_cen"] = input_data["relacion_her_2_cen"]
        processed_data["n°_de_copias"] = input_data["n°_de_copias"]
        processed_data["perfil_molecular"] = input_data["perfil_molecular"]
        processed_data["esquema"] = input_data["esquema"]

        return processed_data

    def predict(self, input_data):
        processed_data = self.preprocessing(input_data)
        return self.dsgd.predict(processed_data)
