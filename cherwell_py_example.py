from cherwell.client import CherwellClient

from cherwell.models import BusinessObject, BusinessObjectFields


if __name__ == '__main__':
    c = CherwellClient('http://172.18.143.91/CherwellAPI')
    token = c.authenticate(
        cid='f9610046-adf6-46a4-8951-19279705f5e8',
        user='analista.eventos',
        pwd='cloudtotvs386'
    )

    data = BusinessObject('939e9d171ec20489a3f7a24484abb9699ddc3d90b9')
    data.fields = [
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:939e9d1df02e2dcf33a3c346e88164db81e7279bf3",
          name="CICondition",
          value="CRITICAL",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:9426c836755ac80098a2314a41a1a40187d2b7173c",
          name="DataDoAlerta",
          value="10/03/2018",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:939e9d1b172ad1896e09b345e7aae49c9971828b53",
          name="Hostname",
          value="test-server",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:939ed00996f287ee50993141cc970f90ce1a241dbd",
          name="IPAddress",
          value="string",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:939e9d1b64da2abd12c2d342dc8b2831fd6ada566c",
          name="Message",
          value="test",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:9429466b0a4aa9f0b0cea64550950ca1f6f8955efe",
          name="Resultado",
          value="test",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:9426e9a62951ec6cb7134943efa9a798c500f45da3",
          name="Serviço",
          value="cpu",
          dirty=True
        ),
        BusinessObjectFields(
          fieldId="BO:939e9d171ec20489a3f7a24484abb9699ddc3d90b9,FI:939e9d18bd97cfe8940a7142e5af127ae01de05a22",
          name="Source",
          value="test",
          dirty=True
        )
    ]

    bo = c.save_business_object(
        token=token,
        data=data,
    )

    print(bo)
