# from fastapi import FastAPI
# from app.product.routers import router as product_router

# app = FastAPI()

# app.include_router(product_router)



cursor.execute(f"""
    SELECT Material1,Material2,
        Coalesce(nullif(Material3,NULL), ''),
        Coalesce(nullif(Material4,NULL), ''),
        THICKN_1,THICKN_2,
        Coalesce(nullif(THICKN_3,NULL), ''),
        Coalesce(nullif(THICKN_4,NULL), ''),
        ProcCode
    FROM fmt
    WHERE concat(carline,'_',phase,'_',variant) in ({carline})
    AND color like ({color})
    AND link = %s
""".format(carline=carline, color=color), [link])
op = cursor.fetchall()

if op:
    M1=str(op[0][0]).replace("[","").replace("]","").split("|")[-1]
    M2=str(op[0][1]).replace("[","").replace("]","").split("|")[-1]
    M3=str(op[0][2]).replace("[","").replace("]","").split("|")[-1]
    M4=str(op[0][3]).replace("[","").replace("]","").split("|")[-1]
    T1, T2, T3, T4, proc = op[0][4],op[0][5],op[0][6],op[0][7],op[0][8]

    try:
        if "[" in M1: M1=M1[2:-2]
        if "[" in M2: M2=M2[2:-2]
        if "[" in M3: M3=M3[2:-2]
        if "[" in M4: M4=M4[2:-2]
    except: pass

    cursor.execute(f"""
        SELECT concat(carline,'_',phase,'_',variant)
        FROM fmt
        WHERE ProcCode like %s
        AND Material1 like %s
        AND Material2 like %s
        AND Coalesce(nullif(Material3,NULL), '') like %s
        AND Coalesce(nullif(Material4,NULL), '') like %s
        AND THICKN_1=%s
        AND THICKN_2=%s
        AND Coalesce(nullif(THICKN_3,NULL),'')=%s
        AND Coalesce(nullif(THICKN_4,NULL),'')=%s
        AND concat(carline,'_',phase,'_',variant) not in ({carline})
    """.format(carline=carline),
    [proc, f"%{M1}%", f"%{M2}%", f"%{M3}%", f"%{M4}%", T1, T2, T3, T4])

    res = cursor.fetchall()
    carlines=[i[0] for i in res]
    if not carlines:
        carlines=["NA"]
    matching_carlines=",".join(carlines)