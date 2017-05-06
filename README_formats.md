# FastXML

    ## C++

    - Input
        - Features and labels separate
            - Xf
                - First line: #elements #features
                - Element
                    - `0:0.084556 ... 4277:5.23237`
                    - feature:value
            - Y
                - First line: #elements, #classes
                - Element
                    - `446:1 ... 1482:1`
                    - label:value
    - Output
        - score_map
            - First line: #elements #labels
            - Element
                - `14:0.00333334 ... 7127:0.004`
                - label:probability

    ## Python

    - Input
        - First line: #elements #labels #features
        - Element
            - `1eda326e3532eafa,-2.3501,...,5.28914 /m/01ykh,...,/m/0krfg`
            - imageid,feature1,...,featureN label1,...,label2
    - Output
        -

