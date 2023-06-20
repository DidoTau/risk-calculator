import pandas as pd
import pickle as pkl

from dsgd.DSClassifierMultiQ import DSClassifierMultiQ
# create a class to model DSGD algorithm


class DSGDClassifier:
    """
    Class to model DSGD algorithm


    """

    def __init__(self, class_num=2, min_iter=1, max_iter=200, min_dloss=0.0001, debug_mode=True,
                 num_workers=4, lossfn="MSE", optim="adam", precompute_rules=True, lr=0.001):
        with open('backend/api/classifiers/encoders/dsgd_breast_her_encoder.pkl', 'rb') as f:
            self.encoder = pkl.load(f)
        self.categorical_columns = [
            'status_menop_al_dg', 'ct', 'cn', 'etapa', 'tipo_histologico', 'perfil_molecular']
        self.non_categorical_columns = ['edad', 'imc', 'axila_en_eco',  're',
                                        'rp', 'ki67', 'relacion_her_2_cen', 'n°_de_copias', 'esquema']
        self.model = DSClassifierMultiQ(class_num, min_iter, max_iter, min_dloss,
                                        debug_mode, num_workers, lossfn, optim, precompute_rules, lr)
        self.rules_bin = "backend/api/classifiers/models/fold_dsgd_2_model.dsb"

    def load_rules(self):
        self.model.model.load_rules_bin(self.rules_bin)

    def preprocessing(self, data):
        input_data = pd.DataFrame([data])
        input_data['rp'] = input_data.apply(
            lambda x: 1 if x['rp'] >= 20 else 0, axis=1)
        input_data['re'] = input_data.apply(
            lambda x: 1 if x['re'] >= 20 else 0, axis=1)
        input_data['ki67'] = input_data.apply(
            lambda x: 1 if x['ki67'] >= 20 else 0, axis=1)
        codified_data = self.encoder.transform(
            input_data[self.categorical_columns])

        return pd.concat([input_data[self.non_categorical_columns],
                          pd.DataFrame(codified_data,
                                       columns=self.encoder.get_feature_names_out(self.categorical_columns))], axis=1)

    def postprocessing(self, prediction):
        prediction_prob = prediction[0]
        print(prediction_prob)
        label = "pCR" if prediction_prob >= 0.5 else "NO pCR"
        return {"label": label, "prob": prediction_prob}

    def predict(self, data):
        
        index_fx = lambda col: list(data.columns).index(col)
        return self.model.predict_proba(data)[:,1]

    def make_prediction(self, data):
        preprocess_data = self.preprocessing(data)
  
        prediction = self.predict(preprocess_data.values.tolist())
        return self.postprocessing(prediction)
