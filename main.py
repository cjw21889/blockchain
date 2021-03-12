from block import Block
from chain import BlockChain
from datetime import datetime


def main():
    manufacturer={'transactions':
              [{
                'timestamp':datetime.now().timestamp(),
                'product_id':1,
                'product_serial': 500,
                'name': 'cotton pants',
                'from': 'Manufacturer X',
                'to': 'Transportation X',
                'message': 'good condition',
                'digital signature': 'approved',
                'flagged': 'N'
                },
                {
                'timestamp':datetime.now().timestamp(),
                'product_id':2,
                'product_serial': 501,
                'name': 'cotton shirt',
                'from': 'Manufacturer X',
                'to': 'Transportation X',
                'message': 'good condition',
                'digital signature': 'approved',
                'flagged': 'N'
                },
                {
                'timestamp':datetime.now().timestamp(),
                'product_id':2,
                'product_serial': 502,
                'name': 'cotton shirt',
                'from': 'Manufacturer X',
                'to': 'Transportation X',
                'message': 'good condition',
                'digital signature': 'approved',
                'flagged': 'N'
                }
              ]}
    transportation={'transactions':
              [{
                'timestamp':datetime.now().timestamp(),
                'product_id':1,
                'product_serial': 500,
                'name': 'cotton pants',
                'from': 'Transportation X',
                'to': 'Vendor X',
                'shipping_id': 100,
                'message': 'good condition',
                'digital signature': 'approved',
                'flagged': 'N'
                },
                {
                'timestamp':datetime.now().timestamp(),
                'product_id':2,
                'product_serial': 501,
                'name': 'cotton shirt',
                'from': 'Transportation X',
                'to': 'Vendor X',
                'shipping_id': 101,
                'message': 'good condition',
                'digital signature': 'approved',
                'flagged': 'N'
                },
                {
                'timestamp':datetime.now().timestamp(),
                'product_id':2,
                'product_serial': 502,
                'name': 'cotton shirt',
                'from': 'Transportation X',
                'to': 'Vendor X',
                'shipping_id': 102,
                'message': 'poor condition',
                'digital signature': 'retailer review',
                'flagged': 'Y'
                }
              ]}

    vendor={'transactions':
          [{
            'timestamp':datetime.now().timestamp(),
            'product_id':1,
            'product_serial': 500,
            'name': 'cotton pants',
            'from': 'Vendor X',
            'to': 'Shelf X',
            'receiving_id': 300,
            'message': 'good condition',
            'digital signature': 'approved',
            'flagged': 'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial': 501,
            'name': 'cotton shirt',
            'from': 'Vendor X',
            'to': 'Shelf X',
            'receiving_id': 301,
            'message': 'good condition',
            'digital signature': 'approved',
            'flagged': 'N'
            },
            {
            'timestamp':datetime.now().timestamp(),
            'product_id':2,
            'product_serial': 502,
            'name': 'cotton shirt',
            'from': 'Vendor X',
            'to': 'RTM',
            'receiving_id': 302,
            'message': 'Box Damaged',
            'digital signature': 'rejected',
            'flagged': 'Y'
            }
          ]}

    B = BlockChain()
    a=B.add(manufacturer)
    b=B.add(transportation)
    c=B.add(vendor)
    B.getTransactions('all')
    print(B.getLastBlock())

if __name__=='__main__':
    main()

