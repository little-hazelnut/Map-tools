/*	������Դ����·����ʶ������ʵ��
 * 	Դ�ļ����ƣ�PointToLineMap.java
 *	Ҫ  �㣺
 *		���ݸ�������������KML��ʽ�ļ�,���ɱ�׼�����·�ߣ���google earth�򿪴�KML��
 *		�������PointToLineKML.java
 */
 
import java.io.File;
import java.awt.Desktop;
import java.io.IOException;

public class PointToLineMap{

	private String src = "";
	private String dest = "";
	private File KMLfile = null;
	
	PointToLineMap(String src,String dest){
		this.src = src;
		this.dest = dest;
	}
	
	public void loadKML(){
		Desktop desktop = Desktop.getDesktop();
		try{
			desktop.open(KMLfile);
		}catch(IOException e){
			e.printStackTrace();
		}
	}
	
	public void creatKML(){
		PointToLineKML ptlk = new PointToLineKML(src,dest);
		KMLfile = ptlk.creatKML();
	}
	
	public static void main(String[] args){
		String srcFile = "20131220s1531fzairport_gs_test.txt";
		String destFile = "20131220s1531fzairport_gs_test.kml";
		PointToLineMap ptlm = new PointToLineMap(srcFile,destFile);
		ptlm.creatKML();
		ptlm.loadKML();
	}
	
}