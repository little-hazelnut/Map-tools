/*	������Դ����·����ʶ������ʵ��
 * 	Դ�ļ����ƣ�PointToMarkKML.java
 *	Ҫ  �㣺
 *		���ݸ�������������KML��ʽ�ļ�,�����ݵ����ɱ�ǵ�
 *		����Ϊ��׼GPS�㣬���ɵĵ�Ϊ��׼����� ������google earth ��������ʾ
 */

import java.io.*;

public class PointToMarkKML{

	private String src = "";
	private String dest = "";
	private File srcFile = null;
	private File destFile = null;
	static String FLAG_HIGH = "0"; //KML�б�־��߶�
	
	PointToMarkKML(String src,String dest){
		this.src = src;
		this.dest = dest;
	}

	public File creatKML(){
		srcFile = new File(src);
		destFile = new File(dest);
		try{
			FileInputStream fis = new FileInputStream(srcFile);
			BufferedReader br = new BufferedReader(new InputStreamReader(fis) );
			
			FileOutputStream fos = new FileOutputStream(destFile);
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
			
			String prefixStr = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
								"<kml xmlns=\"http://earth.google.com/kml/2.1\">\n<Folder>\n";

			String suffixStr = "</Folder>\n</kml>";
			String mark_preStr = "\t<Placemark>\n\t\t<Point>\n\t\t\t<coordinates>"; 
			String mark_sufStr = "</coordinates>\n\t\t</Point>\n\t</Placemark>";
			
			bw.write(prefixStr);
			String str;
			String lon; //����
			String lat;	//γ��
			
			while((str=br.readLine())!=null){
					String[] info = str.split(",");
					if(info.length != 16)
						continue;
					lon = info[4];
					lat = info[5];
					str = mark_preStr + lon +","+ lat+"," + FLAG_HIGH + mark_sufStr;
					bw.write(str);
					bw.newLine();
			}
			bw.write(suffixStr);
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