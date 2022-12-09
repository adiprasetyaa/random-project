/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.praktikum5;

import java.util.regex.*;

/**
 *
 * @author PERSONAL
 */
public class Mahasiswa {

    private String nim;
    private String nama;
    private String email;
    private int angkatan;
    private String jenis_kelamin;

    public Mahasiswa(String nim, String nama, String email, int angkatan, String jenis_kelamin) {
        this.nama = nama;
        this.angkatan = angkatan;
        if(!checkNIM(nim, angkatan)){
            System.out.println("NIM [" + nim + "] input invalid. Data cannot be added.");
        }
        if(!checkJenisKelamin(jenis_kelamin)){
            System.out.println("Gender [" + jenis_kelamin + "] input invalid. Data cannot be added.");
        }
        if(!checkEmail(email)){
            System.out.println("Email [" + email + "] input invalid. Data cannot be added.");
        }
        if(checkNIM(nim, angkatan) && checkJenisKelamin(jenis_kelamin) && checkEmail(email)){
            System.out.println("Data [" + nim + " - " + nama + " - " + angkatan + " - " + jenis_kelamin + " - " + email + "] is added.");
            this.nim = nim;
            this.jenis_kelamin = jenis_kelamin;
            this.email = email;
        }
    }
    
    public void setNIM(String nim){
        if(!checkNIM(nim, angkatan)){
            System.out.println("NIM [" + nim + "] input invalid. Data cannot be added.");
        }else{
            this.nim = nim;
        }
    }
    
    public String getNIM(){
        return this.nim;
    }
    
    public void setNama(String nama){
        this.nama = nama;
    }
    
    public String getNama(){
        return this.nama;
    }
    
    public void setEmail(String email){
        if(!checkEmail(email)){
            System.out.println("Email [" + email + "] input invalid. Data cannot be added.");
        }else{
            this.email = email;
        }
    }
    
    public String getEmail(){
        return this.email;
    }
    
    public void setAngkatan(int angkatan){
        this.angkatan = angkatan;
    }
    
    public int getAngkatan(){
        return this.angkatan;
    }
    
    public void setJenisKelamin(String jenis_kelamin){
        if(!checkJenisKelamin(jenis_kelamin)){
            System.out.println("Gender [" + jenis_kelamin + "] input invalid. Data cannot be added.");
        }else{
          this.jenis_kelamin = jenis_kelamin;  
        }
    }
    
    public String getJenisKelamin(){
        return this.jenis_kelamin;
    }
    
    @Override
    public String toString(){
        return nim + " - " + nama + " - " + angkatan + " - " + jenis_kelamin + " - " + email;
    }

    public boolean checkNIM(String nim, int angkatan) {

        String angkatan_s;
        if (angkatan == 2022) {
            if(nim.matches("L0122[0-2]{1}[0-9]{2}")){
                return true;
            }else{
                return false;
            }
        }else{
            String s_pattern = "M01";
            angkatan_s = Integer.toString(angkatan);
            String angkatan_s2 = angkatan_s.substring(2, 4);
            String pattern = s_pattern.concat(angkatan_s2).concat("[0-2]{1}[0-9]{2}");
            if(nim.matches(pattern)){
                return true;
            }else{
                return false;
            }
        }
    }
    
    public boolean checkJenisKelamin(String jenis_kelamin){
        Pattern pattern = Pattern.compile("[LP]{1}");
        Matcher mtc = pattern.matcher(jenis_kelamin);
        if(mtc.find()){
            return true;
        }else{
            return false;
        }
    }
    
    public boolean checkEmail(String email){
        Pattern pattern = Pattern.compile("[a-zA-Z0-9]{8,}@student.uns.ac.id");
        Matcher mtc = pattern.matcher(email);
        if(mtc.find()){
            return true;
        }else {
            return false;
        }
    }
}
