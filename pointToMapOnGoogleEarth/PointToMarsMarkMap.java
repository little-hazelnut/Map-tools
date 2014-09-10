/*	程序来源：道路限速识别论文实验
 * 	源文件名称：PointToMarsMarkMap.java
 *	要  点：
 *		根据标准坐标浮动车数据生成KML格式文件,生成火星坐标路线,用google earth打开此KML。
 *		生成的数据文件为Mars坐标
 *		必须调用PointToMarsMarkKML.java
 */
 
import java.io.File;
import java.awt.Desktop;
import java.io.IOException;

public class PointToMarsMarkMap{

	private String src = "";
	private String dest = "";
	private File KMLfile = null;
	
	PointToMarsMarkMap(String src,String dest){
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
		PointToMarsMarkKML ptmmk = new PointToMarsMarkKML(src,dest);
		KMLfile = ptmmk.creatKML();
	}
	
	public static void main(String[] args){
		String srcFile = "carID2622206.txt";
		String destFile = "carID2622206_mars.kml";
		PointToMarsMarkMap ptmmm = new PointToMarsMarkMap(srcFile,destFile);
		ptmmm.creatKML();
		ptmmm.loadKML();
	}
	
}