import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../services/api.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-agenda',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './agenda.component.html',
  styleUrls: ['./agenda.component.css']
})
export class AgendaComponent implements OnInit {
  activeTab: string = 'horarios';
  agendamentos: any[] = [];
  nomeBarbeiro: string = 'Admin';
  barberId: number = 0;

  // Financeiro
  faturamentoTotal: number = 0;
  agendamentosHoje: any[] = [];
  chart: any; 

  // Configurações
  config = {
    open_time: '08:00',
    close_time: '18:00',
    lunch_start: '12:00',
    lunch_end: '13:00'
  };
  
  listaServicos: any[] = [];
  
  // Objeto para o formulário de NOVO serviço
  novoServico = {
    name: '',
    price: null,
    duration: 30
  };

  constructor(
    private api: ApiService, 
    private router: Router,
    private cd: ChangeDetectorRef 
  ) {}

  ngOnInit() {
    this.nomeBarbeiro = localStorage.getItem('user_name') || 'Administrador';
    const storedId = localStorage.getItem('user_id');

    if (storedId) {
      this.barberId = Number(storedId);
      this.carregarAgenda();
    } else {
      this.router.navigate(['/login']);
    }
  }

  getTituloPagina(): string {
    switch(this.activeTab) {
      case 'horarios': return 'Agenda Geral';
      case 'faturamento': return 'Painel Financeiro';
      case 'configuracoes': return 'Ajustes';
      default: return 'Painel';
    }
  }

  mudarAba(novaAba: string) {
    this.activeTab = novaAba;
    
    if (novaAba === 'horarios') this.carregarAgenda(false);
    if (novaAba === 'faturamento') setTimeout(() => this.renderizarGrafico(), 100);
    if (novaAba === 'configuracoes') this.carregarConfiguracoes();
  }

  // --- AGENDA ---
  carregarAgenda(showLoading = true) {
    if (showLoading) {
      const Toast = Swal.mixin({ toast: true, position: 'top-end', showConfirmButton: false, timer: 3000, timerProgressBar: true });
      Toast.fire({ icon: 'info', title: 'Atualizando agenda...' });
    }
    this.api.getBarberAgenda(this.barberId).subscribe({
      next: (data) => {
        this.agendamentos = data;
        this.calcularFinanceiro();
        this.cd.detectChanges();
      },
      error: () => Swal.fire('Erro', 'Falha ao carregar dados.', 'error')
    });
  }

  // --- FINANCEIRO ---
  calcularFinanceiro() {
    const hoje = new Date().toISOString().split('T')[0];
    this.agendamentosHoje = this.agendamentos.filter(a => a.date_time.startsWith(hoje));
    this.faturamentoTotal = this.agendamentos.reduce((acc, curr) => acc + (curr.service_price || 0), 0);
  }

  renderizarGrafico() {
    if (this.chart) this.chart.destroy();
    const ctx = document.getElementById('financeChart') as HTMLCanvasElement;
    if (!ctx) return;

    const dadosPorDia: any = {};
    this.agendamentos.forEach(a => {
      const dia = a.date_time.split('T')[0].split('-')[2] + '/' + a.date_time.split('T')[0].split('-')[1];
      if (!dadosPorDia[dia]) dadosPorDia[dia] = 0;
      dadosPorDia[dia] += (a.service_price || 0);
    });

    this.chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: Object.keys(dadosPorDia),
        datasets: [{ label: 'Receita (R$)', data: Object.values(dadosPorDia), backgroundColor: '#00264d', borderRadius: 5 }]
      },
      options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true } } }
    });
  }

  // --- CONFIGURAÇÕES & SERVIÇOS ---
  carregarConfiguracoes() {
    this.api.getSettings().subscribe(data => this.config = data);
    this.carregarListaServicos(); // Separado para poder recarregar sozinho
  }

  carregarListaServicos() {
    this.api.getServices().subscribe(data => this.listaServicos = data);
  }

  salvarHorarios() {
    this.api.updateSettings(this.config).subscribe({
      next: () => Swal.fire('Sucesso', 'Horário atualizado!', 'success'),
      error: () => Swal.fire('Erro', 'Erro ao salvar.', 'error')
    });
  }

  // Atualiza um serviço existente
  salvarServico(servico: any) {
    this.api.updateService(servico.id, servico).subscribe({
      next: () => {
        const Toast = Swal.mixin({ toast: true, position: 'top-end', showConfirmButton: false, timer: 2000 });
        Toast.fire({ icon: 'success', title: 'Preço atualizado' });
      },
      error: () => Swal.fire('Erro', 'Não foi possível atualizar.', 'error')
    });
  }

  // Adiciona um novo serviço
  adicionarServico() {
    if (!this.novoServico.name || !this.novoServico.price) {
      Swal.fire('Atenção', 'Preencha nome e preço.', 'warning');
      return;
    }

    this.api.createService(this.novoServico).subscribe({
      next: () => {
        Swal.fire('Criado!', 'Novo serviço adicionado.', 'success');
        this.novoServico = { name: '', price: null, duration: 30 }; // Limpa form
        this.carregarListaServicos(); // Recarrega lista
      },
      error: () => Swal.fire('Erro', 'Erro ao criar serviço.', 'error')
    });
  }

  logout() {
    Swal.fire({
      title: 'Sair?', showCancelButton: true, confirmButtonText: 'Sim', confirmButtonColor: '#d33'
    }).then((res) => {
      if (res.isConfirmed) { localStorage.clear(); this.router.navigate(['/login']); }
    });
  }
}