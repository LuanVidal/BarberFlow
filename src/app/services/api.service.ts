import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  // Endereço do seu Backend Python
  // Se estiver rodando localmente na porta 5000
  private apiUrl = 'http://127.0.0.1:5000/api'; 

  constructor(private http: HttpClient) { }

  // --- AUTENTICAÇÃO ---
  login(credentials: {email: string, password: string}): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login`, credentials);
  }

  register(userData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register`, userData);
  }

  // --- EXEMPLO: Buscar Barbeiros ---
  getBarbeiros(): Observable<any> {
    return this.http.get(`${this.apiUrl}/barbers/`);
  }
}