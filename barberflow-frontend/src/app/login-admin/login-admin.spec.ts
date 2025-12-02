import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-login-admin',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="login-container" style="background-color: #333;"> <div class="card">
        <h2>🔒 Área Restrita</h2>
        <p>Acesso exclusivo do Barbeiro</p>

        <form (ngSubmit)="login()">
          <input type="email" [(ngModel)]="creds.email" name="email" placeholder="Email Admin">
          <input type="password" [(ngModel)]="creds.password" name="senha" placeholder="Senha">

          <p style="color:red" *ngIf="error">{{ error }}</p>

          <button type="submit">Acessar Agenda</button>
        </form>
        <br>
        <a routerLink="/login">Voltar ao site</a>
      </div>
    </div>
  `,
  styles: [`
    .login-container { display: flex; justify-content: center; align-items: center; height: 100vh; color: #333; }
    .card { background: white; padding: 2rem; border-radius: 8px; width: 300px; text-align: center; }
    input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; }
    button { width: 100%; padding: 10px; background: #000; color: white; border: none; cursor: pointer; }
  `]
})
export class LoginAdminComponent {
  creds = { email: '', password: '' };
  error = '';

  constructor(private api: ApiService, private router: Router) {}

  login() {
    this.api.loginBarber(this.creds).subscribe({
      next: (res: any) => {
        localStorage.setItem('user_id', res.user_id);
        localStorage.setItem('role', 'barber');
        this.router.navigate(['/agenda']); // Manda para a Agenda
      },
      error: () => this.error = 'Acesso negado.'
    });
  }
}