/*	程序来源：道路限速识别论文实验
 * 	源文件名称：PointToLineMap.java
 *	要  点：
 *		根据浮动车数据生成KML格式文件,生成标准坐标点路线，用google earth打开此KML。
 *		必须调用PointToLineKML.java
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