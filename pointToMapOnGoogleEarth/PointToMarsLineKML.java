/*	程序来源：道路限速识别论文实验
 * 	源文件名称：PointToMarsLineKML.java
 *	要  点：
 *		根据浮动车数据生成KML格式文件,由数据点生成路线
 *		输入为标准GPS点，生成的点为火星坐标点，可在国内地图上正常显示
 */

import java.io.*;

public class PointToMarsLineKML{

	private String src = "";
	private String dest = "";
	private File srcFile = null;
	private File destFile = null;
	static String FLAG_HIGH = "50"; //KML中标志点高度
	
	PointToMarsLineKML(String src,String dest){
		this.src = src;
		this.dest = dest;
	}

	public File creatKML(){
		srcFile = new File(src);
		destFile = new File(dest);
		GampOffset goff = new GampOffset();
		try{
			FileInputStream fis = new FileInputStream(srcFile);
			BufferedReader br = new BufferedReader(new InputStreamReader(fis) );
			
			FileOutputStream fos = new FileOutputStream(destFile);
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
			
			String prefixStr = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
								"<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n<Document>\n"+
								"<name>Paths</name>\n<description>Examples of paths. Note that the tessellate tag is by default\n"+
								"set to 0. If you want to create tessellated lines, they must be authored\n"+
								"(or edited) directly in KML.</description>\n"+
								"<Style id=\"yellowLineGreenPoly\">\n"+
								"<LineStyle>\n"+
									"\t<color>7f00ffff</color>\n"+
									"\t<width>4</width>\n"+
								"</LineStyle>\n"+
								"<PolyStyle>\n"+
								"<color>7f00ff00</color>\n"+
								"</PolyStyle>\n"+
								"</Style> <Placemark>\n"+
								"<name>Absolute Extruded</name>\n"+
								"<description>Transparent green wall with yellow outlines</description>\n"+
								"<styleUrl>#yellowLineGreenPoly</styleUrl>\n"+
								"<LineString>\n"+
									"\t<extrude>1</extrude>\n"+
									"\t<tessellate>1</tessellate>\n"+
									"\t<altitudeMode>absolute</altitudeMode>\n"+
								"<coordinates>\n" ;

			String endStr = "</coordinates>\n"+
							"</LineString> </Placemark>\n"+
							"</Document> </kml>";
			
			bw.write(prefixStr);
			String str;
			String lon; //经度
			String lat;	//纬度
			float lng_float = 0.0f;
			float lat_float = 0.0f;
			
			while((str=br.readLine())!=null){
					String[] info = str.split(",");
					if(info.length != 16)
						continue;
					lng_float = Float.parseFloat(info[4]);
					lat_float = Float.parseFloat(info[5]);
					float[] lnglat = goff.wgs2Mars(lng_float,lat_float);
					str = lnglat[0] +","+ lnglat[1]+"," + FLAG_HIGH;
					bw.write(str);
					bw.newLine();
			}
			bw.write(endStr);
			br.close();
			fis.close();
			bw.close();
			fos.close();
		}catch(Exception e){
			e.printStackTrace();
		}
		return destFile;
	}


}