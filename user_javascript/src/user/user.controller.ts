import { Controller, Get, Request, UseGuards } from '@nestjs/common';
import { ApiBearerAuth, ApiTags } from '@nestjs/swagger';
import { JwtAuthGuard } from '../auth/jwt-auth.guard';

@ApiTags('user')
@Controller('user')
export class UserController {
  @ApiBearerAuth()
  @UseGuards(JwtAuthGuard)
  @Get('/current-user')
  getCurrentUser(@Request() req) {
    const user = req.user;

    return {
      language: 'javascript',
      success: true,
      message: 'Get current user successfully',
      current_user: user,
    };
  }
}
