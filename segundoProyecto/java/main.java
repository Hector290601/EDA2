import java.io.*;

public class main {
	static class Paralelo implements Runnable{
		long num = Thread.currentThread().getId();
		@Override
		public void run(){
		}
		long factorial(int n){
			long fact = (long) 1;
			for(int i = 1; i <= (int)((double)n/(double)this.num); i+= (int) this.num){
				fact *= i;
			}
			return fact;
		}
		double euler(int n){
			long fact = (long) 0;
			double div, e = (double) 0;
			for(int i = 0; i <= n; i++){
				fact = factorial(i);
				div = ((double)1/fact);
				e += div;
			}
			return e;
		}
	}
	static class Serial{
		void Serial(){
		}
		long factorial(int n){
			long fact = (long) 1;
			for(int i = 1; i <= n; i++){
				fact *= i;
			}
			return fact;
		}
		double euler(int n){
			long fact = (long) 0;
			double div, e = (double) 0;
			for(int i = 0; i <= n; i++){
				fact = factorial(i);
				div = ((double)1/fact);
				e += div;
			}
			return e;
		}
	}
	static String generateValues(int size){
		Serial serial = new Serial();
		Paralelo obj = new Paralelo();
		Thread th1 = new Thread(obj);
		Thread th2 = new Thread(obj);
		Thread th3 = new Thread(obj);
		Thread th4 = new Thread(obj);
		Thread th5 = new Thread(obj);
		String contenido = "";
		long startSerial, endSerial, startParallel, endParallel;
		double totalSerial, totalParallel, fct = 0, factsParallel[] = {0, 0, 0, 0, 0};
		int millon = 1_000_000_000;
		startSerial = System.nanoTime();
		fct = serial.euler(size);
		endSerial = System.nanoTime();
		totalSerial = ((double)(endSerial - startSerial) / millon);
		contenido += String.valueOf(fct) + "," + String.valueOf(totalSerial) + "," + size + "\n";
		fct = 0;
		startParallel = System.nanoTime();
		th1.start();
		th2.start();
		th3.start();
		th4.start();
		th5.start();
		for(int i = 0; i < 5; i++){
			factsParallel[i] = obj.euler(size/5);
		}
		for(int i = 0; i < 5; i++){
			fct += factsParallel[i];
		}
		fct /= 5;
		endParallel = System.nanoTime();
		totalParallel = ((double)(endParallel - startParallel) / millon);
		contenido += String.valueOf(fct) + "," + String.valueOf(totalParallel) + "," + size + "\n";
		return contenido;
	}
	public static void main(String[] args){
		String ruta = "../dataJava.csv";
		String contenido = "";
		for(int i = 0; i <= 10000; i+=1){
			contenido += generateValues(i);
			System.out.print("Java: ");
			System.out.println(i);
		}
		try{
			PrintWriter writer = new PrintWriter(ruta, "UTF-8");
			writer.println(contenido);
			writer.close();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
}
