
# encoding: utf-8 
'''
Created on 2013年12月18日

@author: NOAH

骆峰式转换字符串

'''


def toCamal(str):
	a=str.lower()
	index=a.find("_");
	return a if index==-1 else a[0:index]+a[index+1].upper()+toCamal(a[index+2:len(a)])

if __name__ == '__main__':	
  '''test the push2'''
	fieldStr="REC_UID,DEVICE_ID,OBJ_ID,RECORD_TIME,SAMPLE_TIME,VIN,FUEL_TYPE,OBD_STD,VEHICLE_SPEED,ENGINE_RPM,FUEL_PRESSURE,DISTANCE_TOTAL,LATEST_ENGINE_RUNTIME,TROUBLE_CODE,DISTANCE_AFTER_MIL,DISTANCE_AFTER_CLEAR_CODE,STATUS_ANGLE_SIDEROLL,STATUS_ANGLE_FORWARDROLL,TIRE_PRESSURE_LEFTFRONT,TIRE_PRESSURE_LEFTREAR,TIRE_PRESSURE_RIGHTFRONT,TIRE_PRESSURE_RIGHTREAR,CARRY_WEIGHT,SAFETYBELT_STATUS,STORAGE_BATTERY_VOLTAGE,ENGINE_COOLLIQUID_TEMP,ENGINE_INLETPORT_TEMP,OUTSIDE_AIR_TEMP,AIR_THROTTLE_POSITION,OXYSENSOR_OUTPUT_VOLTAGE,CALCU_LOAD,POS_TIME,POS_PRECISION,POS_LONGITUDE,POS_LATITUDE,POS_ALTITUDE,POS_SPEED,POS_DIRECTION,ACC_FORWARD,ACC_SIDE,ACC_VERTICAL,STATUS_ANGLE_FORWARD,STATUS_ANGLE_SIDE,STATUS_ANGLE_VERTICAL,GID,STATUS_BASEANGLE_STATUS,STATUS_BASEANGLE_TIME,STATUS_BASEANGLE_FORWARD,STATUS_BASEANGLE_SIDE,STATUS_BASEANGLE_VERTICAL,GAS_PEDAL_POSITION,BRAKE_PEDAL_STATUS,THROTTLE_POSITION,STATUS_LEFT_LIGHT,STATUS_RIGHT_LIGHT,STATUS_DOORS,STATUS_FUELLOW,STATUS_ABM,GATE_NO,FUEL_CONSUMPTION,STATUS_WINDOWS,STATUS_HOOD,STATUS_SKYLIGHT,STATUS_TRUNK,STATUS_HEADLIGHT,TIRE_PRESSURE_LEFTFRONT_STATUS,TIRE_PRESSURE_LEFTREAR_STATUS,TIRE_PRESSURE_RIGHTFRONT_STATUS,TIRE_PRESSURE_RIGHTREAR_STATUS,STATUS_FAR_LIGHT,STATUS_NEAR_LIGHT,STATUS_BRAKE_LIGHT,STATUS_BRUME_LIGHT,STATUS_FRAME_LIGHT,VEHICLE_LOCK,BRAKE_LINING,ENGINE_OIL,GEAR_OIL,TOTAL_MAF,AIR_FLOW_RATE,INTAKE_MANIFOLD_PRESSURE,STATUS_BACK_LIGHT,NEXT_MAINTENANCE_MIL,TODAY_FUEL_CONSUMPTION,LAST_FUEL_CONSUMPTION,STATUS_TROUBLE_LIGHT,ENGINE_DTC_NUMBER,OIL_PRESSURE,BAROMETRIC_PRESSURE,LONGTERM_FUEL_TRIM,SPARK_ANGLE,TOTAL_FUEL_CONSUMPTION,FUEL_PER_HOUR,INSTANT_FUEL_CONSUMPTION"
	fields=fieldStr.split(",")
	a=reduce(lambda a,b:a+' + sperator +'+b,[toCamal(a) for a in fields])
	print a
