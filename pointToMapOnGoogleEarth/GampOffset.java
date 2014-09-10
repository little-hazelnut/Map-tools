/*	程序来源：道路限速识别论文
 * 	源文件名称：GampOffset.java
 *	要	点：
 *		wgs2Mars 提供标准坐标到火星坐标的转换
 *		Mars2wgs 提供火星坐标到标准坐标的转换
 *		参数	lng经度 lat纬度
 */


import java.io.*;
import java.util.*;

public class GampOffset{
	Map<String,String> offset_map = new HashMap<String,String>(20480);
	public GampOffset(){
		String str = null;
		try{
			BufferedReader bw = new BufferedReader(new InputStreamReader(new FileInputStream("fj_offset.txt")));
			while((str = bw.readLine())!= null){
				String[] strs = str.split(",");
				offset_map.put(strs[0]+strs[1],strs[2]+","+strs[3]);
			}
		}catch(IOException e){
			e.printStackTrace();
		}
	}
	
	public float[] wgs2Mars(float lng,float lat){
		int lnground = (int)(lng*100);
		int latround = (int)(lat*100);
		String keyStr = "" + lnground + latround;
		String[] lnglat = offset_map.get(keyStr).split(",");
		float lng_offset = lng + Float.parseFloat(lnglat[0]);
		float lat_offset = lat + Float.parseFloat(lnglat[1]);
		float[] offset_result = new float[2];
		offset_result[0] = lng_offset;
		offset_result[1] = lat_offset;
		return offset_result;
	}
	
	public float[] mars2Wgs(float lng,float lat){
		int lnground = (int)(lng*100);
		int latround = (int)(lat*100);
		String keyStr = "" + lnground + latround;
		String[] lnglat = offset_map.get(keyStr).split(",");
		float lng_offset = lng - Float.parseFloat(lnglat[0]);
		float lat_offset = lat - Float.parseFloat(lnglat[1]);
		float[] offset_result = new float[2];
		offset_result[0] = lng_offset;
		offset_result[1] = lat_offset;
		return offset_result;
	}
	
	/*
	public static void main(String[] args){
		GampOffset goff  = new GampOffset();
		float[] result;
		//result = goff.wgs2Mars(119.355759f,26.1078699f);
		//System.out.println(result[0]+","+result[1]);
		result = goff.mars2Wgs(119.219f,26.0317f);
		System.out.println(result[0]+","+result[1]);
		result = goff.mars2Wgs(119.263f,26.0095f);
		System.out.println(result[0]+","+result[1]);
	}
	*/
	
}

