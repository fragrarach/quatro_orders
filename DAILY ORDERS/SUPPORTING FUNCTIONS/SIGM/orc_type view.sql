DROP VIEW IF EXISTS public.orc_type;
CREATE OR REPLACE VIEW orc_type AS (
    SELECT
            1 as orc_type_idx,
            TRIM(orc_type1) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            2 as orc_type_idx,
            TRIM(orc_type2) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            3 as orc_type_idx,
            TRIM(orc_type3) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            4 as orc_type_idx,
            TRIM(orc_type4) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            5 as orc_type_idx,
            TRIM(orc_type5) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            6 as orc_type_idx,
            TRIM(orc_type6) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            7 as orc_type_idx,
            TRIM(orc_type7) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            8 as orc_type_idx,
            TRIM(orc_type8) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            9 as orc_type_idx,
            TRIM(orc_type9) as orc_type
    FROM order_config
    UNION ALL
    SELECT
            10 as orc_type_idx,
            TRIM(orc_type10) as orc_type
    FROM order_config
)