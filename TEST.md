| TEST # | recipe_P3960_sku0000_MOD_offline.xml | recipe_E4747_sku0000_MOD_offline.xml | recipe_E4747_sku0000_FCT_offline.xml | recipe_P3834_sku0008_MOD_offline.xml | recipe_P3834_sku0001_FCT_offline.xml | recipe_P3834_sku0008_FCT_offline.xml | recipe_P3970_sku0000_MOD_offline.xml | recipe_PhidgetOps.xml | recipe_P3834_sku0001_MOD_offline.xml | 
| --- | | --- | | --- | | --- | | --- | | --- | | --- | | --- | | --- |
| 1 | Sleep_3_Seconds_BuiltIn_P3960 | ENTRY | ECID_SPEEDO | ENTRY | ECID_SPEEDO | ECID_SPEEDO | Sleep_3_Seconds_BuiltIn_P3970 | Sleep_3_Seconds_BuiltIn E4747 | ENTRY | 
| 2 |  | VRS11_FLASH | I2C_DETECT | VRS11_FLASH | I2C_DETECT | I2C_DETECT |  | Turn Off Phidget | VRS11_FLASH | 
| 3 |  | VRS11_READ | VRS12 | VRS11_READ | VRS12 | VRS12 |  | Sleep_9_Seconds_BuiltIn E4747 | VRS11_READ | 
| 4 |  | VRS12_CHECK_RAILS | QSPI | VRS12_CHECK_RAILS | QSPI | QSPI |  | Turn On Phidget | VRS12_CHECK_RAILS | 
| 5 |  | E3921_ID_EEPROM | INA3221 | P3834_ID_EEPROM | INA3221 | INA3221 |  | Sleep_3_Seconds_BuiltIn E4747 | P3834_ID_EEPROM | 
| 6 |  | E3925_ID_EEPROM | EXIT | EXIT | EXIT | EXIT |  | Turn Off Phidget | EXIT | 
| 7 |  | EXIT |  |  |  |  |  |  |  | 
