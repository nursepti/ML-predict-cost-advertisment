# ML-predict-cost-advertisment
predict the advertising costs they need to spend based on sales targets. The data used to predict this is as follows:

Sales.txt data which has 2 columns, namely: Sales and Advertising (million $)
https://www.econometrics.com/intro/sales.htm

# Steps
1. Develop model then save model as a pickle file `regression.pkl` from this 'https://colab.research.google.com/drive/1uwGLetB0spwJDJgPXWju1xXg41P7e22O?usp=sharing'
2. Create new Python virtual environment
3. Activate Python virtual environment `source <nameofenv>/Scipts/activate`
4. Install Python libraries `pip install -r requirements.txt`
5. Run `python regression_endpoint.py`
6. Open browser and go to `localhost:5010/predict-advertising?sales=`