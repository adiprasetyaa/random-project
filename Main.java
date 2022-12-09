/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.praktikum5;

import java.util.*;

/**
 *
 * @author PERSONAL
 */
public class Main {
    
    public void tryValid(){
        Mahasiswa mhs = new Mahasiswa("M0119058", "John Edd", "johnnedd@student.uns.ac.id", 2019, "L");
    }
    
    public void tryInvalidNIM(){
        Mahasiswa mhs = new Mahasiswa("M0121390", "Putri Rizqi", "putririzqik@student.uns.ac.id", 2021, "P");
    }
    
    public void tryInvalidJenisKelamin(){
        Mahasiswa mhs = new Mahasiswa("L0122003", "Elizabeth Jane", "elizjane@student.uns.ac.id", 2022, "F");
    }
    
    public void tryInvalidEmail(){
        Mahasiswa mhs = new Mahasiswa("M0120056", "Jack Sparrow", "jacksparr@student.its.ac.id", 2020, "P");
    }
    
    public void tryInvalidAll(){
        Mahasiswa mhs = new Mahasiswa("K0521390", "Daehwi Lee", "daehwilee@student.uns.solo.id", 2019, "X");
    }
    
    public void arrayOfObjects(Mahasiswa mhs[]){
        
        // Add data
        System.out.println("\nAdd Data");
        mhs[0] = new Mahasiswa("M0118010", "Amber Lee", "amberlee@student.uns.ac.id", 2018, "P");
        mhs[1] = new Mahasiswa("M0119077", "Mikaela", "mikaela7@student.uns.ac.id", 2019, "P");
        mhs[2] = new Mahasiswa("M0120053", "Rajendrana", "jendraaa@student.uns.ac.id", 2020, "L");
        mhs[3] = new Mahasiswa("M0121041", "Raka Prawira", "rakapraw@student.uns.ac.id", 2021, "L");
        mhs[4] = new Mahasiswa("L0122276", "Billie", "billie02@student.uns.ac.id", 2022, "L");
        mhs[5] = new Mahasiswa("L0122195", "Arzha Diandrana", "zhaazraa@student.uns.ac.id", 2022, "P");
        mhs[6] = new Mahasiswa("L0122107", "Ranjaya", "ranjayaya@student.uns.ac.id", 2022, "L");
        mhs[7] = new Mahasiswa("M0119222", "Dhiza Khaya", "dhizakha@student.uns.ac.id", 2019, "P");
        mhs[8] = new Mahasiswa("M0120111", "Lee Manbok", "bokmanha@student.uns.ac.id", 2020, "L");
        mhs[9] = new Mahasiswa("M0121001", "Shin Youngeun", "youngeun@student.uns.ac.id", 2021, "P");
        
        // Show Array of Objects
        System.out.println("\nShow Array of Objects");
        for(int i = 0; i < mhs.length; i++){
            System.out.println(mhs[i].toString());
        }
    }
    
    public void arrayList(List<Mahasiswa> mhs){
        
        // Add data
        System.out.println("\nAdd Data");
        Mahasiswa mahasiswa;
        mahasiswa = new Mahasiswa("M0118010", "Amber Lee", "amberlee@student.uns.ac.id", 2018, "P");;
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("M0119077", "Mikaela", "mikaela7@student.uns.ac.id", 2019, "P");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("M0120053", "Rajendrana", "jendraaa@student.uns.ac.id", 2020, "L");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("M0121041", "Raka Prawira", "rakapraw@student.uns.ac.id", 2021, "L");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("L0122276", "Billie", "billie02@student.uns.ac.id", 2022, "L");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("L0122195", "Arzha Diandrana", "zhaazraa@student.uns.ac.id", 2022, "P");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("L0122107", "Ranjaya", "ranjayaya@student.uns.ac.id", 2022, "L");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("M0119222", "Dhiza Khaya", "dhizakha@student.uns.ac.id", 2019, "P");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("M0120111", "Lee Manbok", "bokmanha@student.uns.ac.id", 2020, "L");
        mhs.add(mahasiswa);
        mahasiswa = new Mahasiswa("M0121001", "Shin Youngeun", "youngeun@student.uns.ac.id", 2021, "P");
        mhs.add(mahasiswa);
        
        // Show data
        System.out.println("\nShow Data");
        for(int i = 0; i < mhs.size(); i++){
            System.out.println((mhs.get(i)).toString());
        }
    }
    
    public void hashMap(HashMap<Integer,Mahasiswa> mhs){
        
        // Add data
        System.out.println("\nAdd Data");
        mhs.put(18010, new Mahasiswa("M0118010", "Amber Lee", "amberlee@student.uns.ac.id", 2018, "P"));
        mhs.put(19077, new Mahasiswa("M0119077", "Mikaela", "mikaela7@student.uns.ac.id", 2019, "P"));
        mhs.put(20053, new Mahasiswa("M0120053", "Rajendrana", "jendraaa@student.uns.ac.id", 2020, "L"));
        mhs.put(21041, new Mahasiswa("M0121041", "Raka Prawira", "rakapraw@student.uns.ac.id", 2021, "L"));
        mhs.put(22276, new Mahasiswa("L0122276", "Billie", "billie02@student.uns.ac.id", 2022, "L"));
        mhs.put(22195, new Mahasiswa("L0122195", "Arzha Diandrana", "zhaazraa@student.uns.ac.id", 2022, "P"));
        mhs.put(22107, new Mahasiswa("L0122107", "Ranjaya", "ranjayaya@student.uns.ac.id", 2022, "L"));
        mhs.put(19222, new Mahasiswa("M0119222", "Dhiza Khaya", "dhizakha@student.uns.ac.id", 2019, "P"));
        mhs.put(20111, new Mahasiswa("M0120111", "Lee Manbok", "bokmanha@student.uns.ac.id", 2020, "L"));
        mhs.put(21001, new Mahasiswa("M0121001", "Shin Youngeun", "youngeun@student.uns.ac.id", 2021, "P"));
        
        // Show data
        System.out.println("\nShow Data");
        for(Map.Entry hm : mhs.entrySet()){
            System.out.println("[" + hm.getKey() + "] " + (hm.getValue()).toString());
        }
    }
    
    public void treeMap(TreeMap<Integer,Mahasiswa> mhs){
        
        // Add data
        System.out.println("\nAdd Data");
        mhs.put(18010, new Mahasiswa("M0118010", "Amber Lee", "amberlee@student.uns.ac.id", 2018, "P"));
        mhs.put(19077, new Mahasiswa("M0119077", "Mikaela", "mikaela7@student.uns.ac.id", 2019, "P"));
        mhs.put(20053, new Mahasiswa("M0120053", "Rajendrana", "jendraaa@student.uns.ac.id", 2020, "L"));
        mhs.put(21041, new Mahasiswa("M0121041", "Raka Prawira", "rakapraw@student.uns.ac.id", 2021, "L"));
        mhs.put(22276, new Mahasiswa("L0122276", "Billie", "billie02@student.uns.ac.id", 2022, "L"));
        mhs.put(22195, new Mahasiswa("L0122195", "Arzha Diandrana", "zhaazraa@student.uns.ac.id", 2022, "P"));
        mhs.put(22107, new Mahasiswa("L0122107", "Ranjaya", "ranjayaya@student.uns.ac.id", 2022, "L"));
        mhs.put(19222, new Mahasiswa("M0119222", "Dhiza Khaya", "dhizakha@student.uns.ac.id", 2019, "P"));
        mhs.put(20111, new Mahasiswa("M0120111", "Lee Manbok", "bokmanha@student.uns.ac.id", 2020, "L"));
        mhs.put(21001, new Mahasiswa("M0121001", "Shin Youngeun", "youngeun@student.uns.ac.id", 2021, "P"));
        
        // Show data
        System.out.println("\nShow Data");
        for(Map.Entry tm : mhs.entrySet()){
            System.out.println("[" + tm.getKey() + "] " + (tm.getValue()).toString());
        }
    }
    
    public static void main(String args[]){
        Main tes = new Main();
        
        System.out.println("NOMOR 1");
        System.out.println("==================== Valid Input ====================");
        tes.tryValid();
        System.out.println();
        
        System.out.println("==================== Invalid NIM Input ====================");
        tes.tryInvalidNIM();
        System.out.println();
        
        System.out.println("==================== Invalid Gender Input ====================");
        tes.tryInvalidJenisKelamin();
        System.out.println();
        
        System.out.println("==================== Invalid Email Input ====================");
        tes.tryInvalidEmail();
        System.out.println();
        
        System.out.println("==================== Invalid All Input ====================");
        tes.tryInvalidAll();
        System.out.println();
        
        System.out.println("NOMOR 2");
        System.out.println("==================== Array of Objects ====================");
        Mahasiswa[] mhs = new Mahasiswa[10];
        tes.arrayOfObjects(mhs);
        System.out.println();
        
        System.out.println("========== Array List ==========");
        List<Mahasiswa> mhs2 = new ArrayList<Mahasiswa>();
        tes.arrayList(mhs2);
        System.out.println();
        
        System.out.println("========== Hash Map ==========");
        HashMap<Integer,Mahasiswa> mhs3 = new HashMap<>();
        tes.hashMap(mhs3);
        System.out.println();
        
        System.out.println("========== Tree Map ==========");
        TreeMap<Integer,Mahasiswa> mhs4 = new TreeMap<>();
        tes.treeMap(mhs4);
        System.out.println();
    }
}
