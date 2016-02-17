import dill as pickle
import pandas as pd
import numpy as np
from sklearn import neighbors, cross_validation, grid_search, base
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import RandomForestRegressor
from sklearn.base import BaseEstimator, TransformerMixin
import matplotlib.pyplot as plt

class NestedDictTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def flatten_dict(self,d,parent_key,sep):
        items = []
        for key, value in d.iteritems():
            new_key = parent_key + sep + key if parent_key else key
            if isinstance(value, dict):
                items.extend(self.flatten_dict(value,new_key,sep=sep).items())
            else:
                items.append((new_key, value))
        return dict(items)
  
    def fit(self, X, y):
        return self

    def transform(self, X):
    
        if isinstance(X,dict):
            return self.flatten_dict(X['attributes'],'','_')
        else:
            return X['attributes'].map(lambda x: self.flatten_dict(x,'','_'))
