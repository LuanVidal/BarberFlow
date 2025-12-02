import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000/api'; 

  constructor(private http: HttpClient) { }

  // --- Auth Cliente ---
  login(credentials: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login`, credentials);
  }
  
  register(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register`, data);
  }

  // --- Auth Barbeiro (O QUE ESTAVA FALTANDO) ---
  loginBarber(credentials: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login-barber`, credentials);
  }

  // --- Dados Gerais ---
  getBarbeiros(): Observable<any> {
    return this.http.get(`${this.apiUrl}/barbers/`);
  }
  
  getServices(): Observable<any> {
    return this.http.get(`${this.apiUrl}/services/`);
  }

  // --- Agendamentos ---
  createAppointment(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/appointments/`, data);
  }

  getBarberAgenda(barberId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/appointments/barber/${barberId}`);
  }

  // Busca agendamentos do CLIENTE (para ver se ele já tem um)
  getUserAppointments(userId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/appointments/user/${userId}`);
  }

  // Cancela
  cancelAppointment(apptId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/appointments/${apptId}`);
  }

  // Busca horários ocupados (para filtrar o select)
  getTakenSlots(barberId: number, date: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/appointments/taken/${barberId}/${date}`);
  }


getSettings(): Observable<any> {
    return this.http.get(`${this.apiUrl}/services/settings`);
  }

  updateSettings(data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/services/settings`, data);
  }

  // Atualizar Serviço
  updateService(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/services/${id}`, data);
  }

  createService(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/services/`, data);
  }

  
}