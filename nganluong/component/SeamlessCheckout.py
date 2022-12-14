import pycurl
import urllib.parse
import hashlib
from io import BytesIO
from nganluong import config
import json
import xmltodict

class SeamlessCheckout:

    def _call(self, params):
        body            = BytesIO()
        headers         = BytesIO()
        crl = pycurl.Curl()
        crl.setopt(pycurl.URL,              config.NL_ENDPOINT)
        crl.setopt(pycurl.FOLLOWLOCATION,   True)
        crl.setopt(pycurl.AUTOREFERER,      True)
        crl.setopt(pycurl.COOKIESESSION,    True)
        crl.setopt(pycurl.SSL_VERIFYHOST,   False)
        crl.setopt(pycurl.SSL_VERIFYPEER,   False)
        crl.setopt(pycurl.CONNECTTIMEOUT,   60)
        crl.setopt(pycurl.TIMEOUT,          60)
        crl.setopt(pycurl.POST,             True)
        crl.setopt(pycurl.POSTFIELDS,       urllib.parse.urlencode(params))
        crl.setopt(pycurl.WRITEDATA,        body)
        crl.setopt(pycurl.HEADERFUNCTION,   headers.write)
        try:
            crl.perform()
            respone             = body.getvalue().decode("utf-8")
            respone_headers     = headers.getvalue().decode("utf-8")
        except:
            respone             = ''
            respone_headers     = ''

        result                  = str(respone).replace('&', '&amp;')
        data_dict               = xmltodict.parse(result)
        json_result             = json.dumps(data_dict)
        result                  = json.loads(json_result)
        body.close()
        headers.close()
        crl.close()
        return result['result']

    def setExpressCheckout(self, params):
        input                       = {
            'merchant_id'           : config.MERCHANT_ID,
            'merchant_password'     : hashlib.md5(config.MERCHANT_PASSWORD.encode()).hexdigest(), #MERCHANT_PASSWORD
            'version'               : config.VERSION,
            'function'              : 'SetExpressCheckout',
            'receiver_email'        : config.RECEIVER_EMAIL,
            'order_code'            : params['order_code'],
            'total_amount'          : params['total_amount'],
            'payment_method'        : params['payment_method'],
            'payment_type'          : config.payment_type,
            'fee_shipping'          : params['fee_shipping'],
            'bank_code'             : params['bank_code'],
            'return_url'            : config.return_url,
            'buyer_fullname'        : params['buyer_fullname'],
            'buyer_email'           : params['buyer_email'],
            'buyer_mobile'          : params['buyer_mobile'],
            'card_number'           : params['card_number'],
            'card_fullname'         : params['card_fullname'],
            'card_month'            : params['card_month'],
            'card_year'             : params['card_year']
        }

        result                      = self._call(input)
        return result

    def authenTransaction(self, params):
        inputs                      = {
            'merchant_id'           : config.MERCHANT_ID,
            'merchant_password'     : hashlib.md5(config.MERCHANT_PASSWORD.encode()).hexdigest(),
            'version'               : config.VERSION,
            'function'              : 'AuthenTransaction',
            'token'                 : params['token'],
            'otp'                   : params['otp'],
            'auth_url'              : params['auth_url']
        }

        result                      = self._call(inputs)
        return result

    def getTransactionDetail(self, params):
        inputs                      = {
            'merchant_id'           : config.MERCHANT_ID,
            'merchant_password'     : hashlib.md5(config.MERCHANT_PASSWORD.encode()),
            'version'               : config.VERSION,
            'function'              : 'GetTransactionDetail',
            'token'                 : params['token']
        }

        result                      = self._call(inputs)
        return result

    def getRequestField(self, params):
        inputs                      = {
            'merchant_id'           : config.MERCHANT_ID,
            'merchant_password'     : hashlib.md5(config.MERCHANT_PASSWORD.encode()).hexdigest(),
            'version'               : config.VERSION,
            'function'              : 'GetRequestField',
            'receiver_email'        : config.RECEIVER_EMAIL,
            # 'payment_method'        : params['payment_method'],
            # 'bank_code'             : params['bank_code']
        }
        result                      = self._call(inputs)
        return result

    def getBankName(self, bank_code):
        list_bank_name              = {
            'AGB'                   : 'Ng??n h??ng N??ng nghi???p v?? Ph??t tri???n N??ng th??n',
            'BAB'                   : 'Ng??n h??ng TMCP B???c ??',
            'BIDV'                  : 'Ng??n h??ng ?????u t?? v?? Ph??t tri???n Vi???t Nam',
            'EXB'                   : 'Ng??n h??ng TMCP Xu???t Nh???p Kh???u',
            'MSB'                   : 'Ng??n h??ng TMCP H??ng H???i',
            'STB'                   : 'Ng??n h??ng TMCP S??i G??n Th????ng T??n',
            'SGB'                   : 'Ng??n h??ng TMCP  S??i G??n C??ng th????ng',
            'NVB'                   : 'Ng??n h??ng TMCP Nam Vi???t',
            'PGB'                   : 'Ng??n h??ng TMCP X??ng D???u Petrolimex',
            'GPB'                   : 'Ng??n h??ng TMCP D???u Kh??',
            'ICB'                   : 'Ng??n h??ng TMCP C??ng Th????ng',
            'TCB'                   : 'Ng??n h??ng TMCP K??? Th????ng',
            'TPB'                   : 'Ng??n h??ng TMCP Ti??n Phong',
            'VAB'                   : 'Ng??n h??ng TMCP Vi???t ??',
            'VIB'                   : 'Ng??n h??ng TMCP Qu???c t???',
            'VCB'                   : 'Ng??n h??ng TMCP Ngo???i Th????ng Vi???t Nam',
            'VCBPAY'                : 'VCBPAY',
            'DAB'                   : 'Ng??n h??ng TMCP ????ng ??',
            'MB'                    : 'Ng??n h??ng TMCP Qu??n ?????i',
            'ACB'                   : 'Ng??n h??ng TMCP ?? Ch??u',
            'HDB'                   : 'Ng??n h??ng TMCP Ph??t Tri???n Nh?? TP.H??? Ch?? Minh',
            'VPB'                   : 'Ng??n h??ng TMCP Vi???t Nam Th???nh V?????ng',
            'OJB'                   : 'Ng??n h??ng TMCP ?????i D????ng',
            'SHB'                   : 'Ng??n h??ng TMCP S??i G??n - H?? N???i',
            'SEA'                   : 'Ng??n h??ng TMCP ????ng Nam ??',
            'OCB'                   : 'Ng??n h??ng Ph????ng ????ng Vi???t Nam',
            'ABB'                   : 'Ng??n h??ng TMCP An B??nh',
            'NAB'                   : 'Ng??n h??ng Nam ??',
            'SCB'                   : 'Ng??n h??ng TMCP S??i G??n',
            'IVB'                   : 'Ng??n h??ng TNHH Indovina',
            'WCP'                   : 'WeChat Pay',
            'VIETTELPOST'           : 'Viettelpost',
        }

        if bank_code in list_bank_name:
            bank_name               = list_bank_name[bank_code]
        else:
            bank_name               = "N/A"

        return bank_name

    def getBanksByPaymentMethod(self, payment_method):

        if (payment_method == "ATM_ONLINE"):
            banks   = [
                'AGB', 'BAB', 'BIDV', 'EXB', 'MSB', 'STB', 'SGB', 'NVB', 'PGB', 'GPB',
                'ICB', 'TCB', 'TPB', 'VAB', 'VIB', 'VCB', 'MB', 'ACB', 'HDB', 'VPB',
                'OJB', 'SHB', 'SEA', 'OCB', 'ABB', 'NAB'
            ]
        elif (payment_method == "IB_ONLINE"):
            banks   = ['BIDV', 'EXB', 'STB', 'ICB', 'TCB', 'VCB', 'DAB', 'ACB']
        elif (payment_method == "QRCODE"):
            banks   = ['AGB', 'MSB', 'NVB', 'ICB', 'VCB', 'VCBPAY', 'MB', 'VPB', 'SHB', 'OCB', 'ABB', 'SCB', 'IVB', 'WCP']
        elif (payment_method == "CASH_IN_SHOP"):
            banks   = ['VIETTELPOST']
        else:
            banks   = []

        bank_info   = {}

        for bank in banks:
            bank_info[bank]     = self.getBankName(bank)

        return bank_info