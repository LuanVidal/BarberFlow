import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-login-admin',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  template: `
    <div class="login-container" style="background-color: #222;">
      <div class="card">
        <h2>🔒 Área do Barbeiro</h2>
        <p>Acesso Administrativo</p>

        <form (ngSubmit)="login()">
          <input type="email" [(ngModel)]="creds.email" name="email" placeholder="Email do Barbeiro">
          <input type="password" [(ngModel)]="creds.password" name="senha" placeholder="Senha">
          
          <p style="color:red" *ngIf="error">{{ error }}</p>
          
          <button type="submit">Entrar na Agenda</button>
        </form>
        <br>
        <a routerLink="/login">Voltar para o site</a>
      </div>
    </div>
  `,
  styles: [`
    .login-container { display: flex; justify-content: center; align-items: center; height: 100vh; color: #333; }
    .card { background: white; padding: 2rem; border-radius: 8px; width: 300px; text-align: center; }
    input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; }
    button { width: 100%; padding: 10px; background: #000; color: white; border: none; cursor: pointer; }
    a { font-size: 0.9em; color: #666; text-decoration: none; }
  `]
})
export class LoginAdminComponent { // <--- ESSA É A LINHA QUE O ERRO DIZ QUE FALTA
  creds = { email: '', password: '' };
  error = '';

  constructor(private api: ApiService, private router: Router) {}

  login() {
    this.api.loginBarber(this.creds).subscribe({
      next: (res: any) => {
        localStorage.setItem('user_id', res.user_id);
        localStorage.setItem('role', 'barber');
        this.router.navigate(['/agenda']);
      },
      error: () => this.error = 'Login falhou. Verifique e-mail e senha.'
    });
  }
}