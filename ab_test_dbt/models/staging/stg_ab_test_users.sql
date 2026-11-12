{{ config(materialized='view') }}

WITH raw_data AS (
    SELECT * FROM {{ source('ab_testing', 'raw_ab_test') }}
)

SELECT 
    user_id,
    test_group AS experiment_variant,
    converted AS is_converted,
    revenue AS conversion_revenue,
    CASE WHEN converted = 1 THEN TRUE ELSE FALSE END AS conversion_flag
FROM raw_data